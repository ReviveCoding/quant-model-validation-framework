import sys
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

import numpy as np
import pandas as pd
from utils import ensure_dirs, project_path, load_yaml, write_csv, write_json, write_md
from data.generate_synthetic_market import generate_synthetic_market, generate_option_portfolio, create_public_sample_files
from data.validate_data_quality import validate_time_series
from data.public_market_data import validate_public_market_data
from models.black_scholes import bs_call_price
from models.binomial_tree import binomial_call_price
from models.monte_carlo_option import mc_call_price
from models.heston_simulation import heston_call_price
from models.vasicek_rates import vasicek_paths, cir_paths
from validation.no_arbitrage_checks import call_no_arbitrage_checks
from validation.greeks_validation import validate_greeks
from validation.convergence_tests import binomial_convergence_case, monte_carlo_convergence_case
from validation.kupiec_test import kupiec_pof_test
from validation.christoffersen_test import christoffersen_independence_test
from validation.exception_analysis import summarize_exceptions
from validation.assumption_sensitivity import assumption_sensitivity
from validation.risk_factor_modellability import risk_factor_modellability_proxy
from validation.stress_scenario_coverage import stress_scenario_coverage
from numerical_reliability.tolerance_gates import apply_tolerance_gate
from numerical_reliability.seed_stability import seed_stability_case
from numerical_reliability.cpu_gpu_consistency import cpu_gpu_consistency_stub
from risk.portfolio_var import historical_var_es, monte_carlo_var_es, rolling_backtest_var
from risk.subportfolio_backtesting import subportfolio_backtests
from risk.stressed_var import stressed_var_window
from risk.pnl_attribution import pnl_attribution_proxy
from risk.apl_hpl_backtesting import apl_hpl_backtesting_proxy
from risk.es_tail_diagnostics import es_tail_diagnostics
from risk.liquidity_horizon_es import liquidity_horizon_es_proxy
from risk.stress_loss import option_portfolio_stress_loss
from risk.full_revaluation import full_revaluation_change, delta_gamma_change
from specialty.residual_error_correction import residual_error_correction
from specialty.asymmetric_validation_envelope import asymmetric_envelope
from specialty.validation_health_score import build_validation_health_score
from governance.model_inventory import inventory_from_config
from governance.finding_severity import build_findings
from governance.release_gate import release_decision
from governance.validation_memo import make_report
from governance.model_card import model_card_text
from governance.known_limitations import limitations_text
from governance.compensating_controls import controls_text
from governance.regulatory_mapping import regulatory_mapping_table
from governance.baseline_final_summary import build_baseline_vs_final_summary
from governance.structure_audit import structure_audit
from governance.artifact_manifest import artifact_manifest, run_manifest


def main():
    ensure_dirs()

    # Data generation and samples
    market = generate_synthetic_market()
    options = generate_option_portfolio()
    create_public_sample_files(project_path('data/public'))
    public_checks, public_summary, public_panel, public_corr = validate_public_market_data(project_path('data/public'))
    write_csv('outputs/public_market_data_validation.csv', public_checks)
    write_csv('outputs/public_risk_factor_summary.csv', public_summary)
    write_csv('outputs/public_risk_factor_panel.csv', public_panel)
    write_csv('outputs/public_risk_factor_correlation.csv', public_corr)
    modellability = risk_factor_modellability_proxy(public_panel)
    write_csv('outputs/risk_factor_modellability_proxy.csv', modellability)
    market.to_csv(project_path('data/synthetic/correlated_asset_returns.csv'), index=False)
    options.to_csv(project_path('data/synthetic/option_portfolio.csv'), index=False)

    data_quality = validate_time_series(market)
    write_csv('outputs/data_quality_report.csv', data_quality)

    # Model inventory
    inventory = inventory_from_config(load_yaml('configs/model_inventory.yaml'))
    write_csv('outputs/model_inventory.csv', inventory)

    # Pricing and benchmark comparisons
    rows = []
    sample = options.head(80).copy()
    for _, row in sample.iterrows():
        bs = float(bs_call_price(row['S'], row['K'], row['T'], row['r'], row['sigma']))
        binom = binomial_call_price(row['S'], row['K'], row['T'], row['r'], row['sigma'], steps=200)
        mc, mc_se = mc_call_price(row['S'], row['K'], row['T'], row['r'], row['sigma'], paths=8000, seed=int(row.name)+11)
        heston = heston_call_price(row['S'], row['K'], row['T'], row['r'], row['sigma']**2, paths=2500, steps=40, seed=int(row.name)+101)
        rows.append({
            'option_id': row['option_id'], 'S': row['S'], 'K': row['K'], 'T': row['T'], 'r': row['r'], 'sigma': row['sigma'],
            'moneyness': row['S'] / row['K'], 'bs_price': bs, 'binomial_price': binom, 'mc_price': mc, 'mc_stderr': mc_se, 'heston_price': heston,
            'binomial_error': binom - bs, 'mc_error': mc - bs, 'heston_error': heston - bs,
            'abs_error': abs(mc - bs), 'rel_abs_error': abs(mc - bs) / max(abs(bs), 1.0), 'risk_underestimation': mc < bs
        })
    benchmark = pd.DataFrame(rows)
    benchmark_gated = apply_tolerance_gate(benchmark, error_col='rel_abs_error', warn=0.05, block=0.15)
    write_csv('outputs/benchmark_comparison.csv', benchmark_gated)

    # Residual error correction and asymmetric validation
    residual_detail, residual_summary = residual_error_correction(benchmark, 'mc_error')
    write_csv('outputs/residual_error_correction_detail.csv', residual_detail)
    write_csv('outputs/residual_error_correction_summary.csv', residual_summary)
    asym = asymmetric_envelope(residual_detail, 'corrected_relative_error', 'risk_underestimation')
    write_csv('outputs/asymmetric_validation_envelope.csv', asym)

    # No-arbitrage and Greeks
    noarb = call_no_arbitrage_checks(benchmark)
    write_csv('outputs/no_arbitrage_checks.csv', noarb)
    greeks = validate_greeks(sample, sample_size=60)
    write_csv('outputs/greeks_validation.csv', greeks)

    # Convergence and numerical reliability
    conv = pd.concat([binomial_convergence_case(), monte_carlo_convergence_case()], ignore_index=True)
    write_csv('outputs/convergence_summary.csv', conv)
    seed_stability = seed_stability_case()
    write_csv('outputs/seed_stability.csv', seed_stability)
    cpu_gpu = cpu_gpu_consistency_stub(float(benchmark['mc_price'].mean()))
    write_csv('outputs/cpu_gpu_consistency.csv', cpu_gpu)

    # Rate model sanity checks
    vas = vasicek_paths(paths=1200)
    cir = cir_paths(paths=1200)
    rates_sanity = pd.DataFrame([
        {'model': 'Vasicek', 'terminal_mean': float(vas[:,-1].mean()), 'terminal_min': float(vas[:,-1].min()), 'negative_rate_share': float((vas < 0).mean())},
        {'model': 'CIR', 'terminal_mean': float(cir[:,-1].mean()), 'terminal_min': float(cir[:,-1].min()), 'negative_rate_share': float((cir < 0).mean())},
    ])
    rates_sanity['status'] = np.where((rates_sanity['model'] == 'CIR') & (rates_sanity['negative_rate_share'] > 0), 'REVIEW', 'PASS')
    write_csv('outputs/rate_model_sanity.csv', rates_sanity)

    # Full revaluation vs delta-gamma
    dg_rows = []
    for _, row in sample.head(50).iterrows():
        dS = -0.03 * row['S']
        full = full_revaluation_change(row['S'], row['K'], row['T'], row['r'], row['sigma'], dS)
        dg = delta_gamma_change(row['S'], row['K'], row['T'], row['r'], row['sigma'], dS)
        dg_rows.append({'option_id': row['option_id'], 'full_revaluation_change': full, 'delta_gamma_change': dg, 'approx_error': dg-full, 'abs_approx_error': abs(dg-full)})
    dg_df = pd.DataFrame(dg_rows)
    write_csv('outputs/full_revaluation_vs_delta_gamma.csv', dg_df)

    # VaR / ES and stress testing
    hvar, hes = historical_var_es(market['portfolio_pnl'], alpha=0.99)
    nvar, nes = monte_carlo_var_es(market['portfolio_pnl'], alpha=0.99, heavy_tail=False)
    tvar, tes = monte_carlo_var_es(market['portfolio_pnl'], alpha=0.99, heavy_tail=True)
    var_es = pd.DataFrame([
        {'method': 'historical', 'VaR_99': hvar, 'ES_99': hes},
        {'method': 'normal_monte_carlo', 'VaR_99': nvar, 'ES_99': nes},
        {'method': 'student_t_monte_carlo', 'VaR_99': tvar, 'ES_99': tes},
    ])
    write_csv('outputs/var_es_results.csv', var_es)
    stressed_var = stressed_var_window(market['portfolio_pnl'], window=250, alpha=0.99, stress_window=60)
    write_csv('outputs/stressed_var_results.csv', stressed_var)
    es_tail = es_tail_diagnostics(market['portfolio_pnl'], var_es, alpha=0.99)
    write_csv('outputs/es_tail_diagnostics.csv', es_tail)
    liquidity_es = liquidity_horizon_es_proxy(market, alpha=0.975)
    write_csv('outputs/liquidity_horizon_es_proxy.csv', liquidity_es)

    stress_cfg = load_yaml('configs/stress_config.yaml')
    stress = option_portfolio_stress_loss(options, stress_cfg['stress_scenarios'])
    write_csv('outputs/stress_loss_results.csv', stress)
    scenario_coverage = stress_scenario_coverage(stress, stress_cfg['stress_scenarios'])
    write_csv('outputs/stress_scenario_coverage.csv', scenario_coverage)

    bt_cfg = load_yaml('configs/backtesting_config.yaml')
    bt = rolling_backtest_var(market['portfolio_pnl'], window=bt_cfg['window'], alpha=bt_cfg['confidence_level'])
    write_csv('outputs/backtesting_exceptions.csv', bt)
    bt_summary = summarize_exceptions(bt)
    write_csv('outputs/backtesting_summary.csv', bt_summary)
    kup = kupiec_pof_test(bt['exception'].sum(), len(bt), alpha=0.99)
    chr_res = christoffersen_independence_test(bt['exception'].astype(int).to_numpy())
    kc = pd.DataFrame([kup, chr_res])
    write_csv('outputs/kupiec_christoffersen_results.csv', kc)

    sub_bt_detail, sub_bt_summary, sub_bt_tests = subportfolio_backtests(market, window=bt_cfg['window'], alpha=bt_cfg['confidence_level'])
    write_csv('outputs/subportfolio_backtesting_detail.csv', sub_bt_detail)
    write_csv('outputs/subportfolio_backtesting_summary.csv', sub_bt_summary)
    write_csv('outputs/subportfolio_backtesting_tests.csv', sub_bt_tests)
    pnl_attr_detail, pnl_attr_summary, pnl_attr_components = pnl_attribution_proxy(market)
    write_csv('outputs/pnl_attribution_proxy_detail.csv', pnl_attr_detail)
    write_csv('outputs/pnl_attribution_proxy_summary.csv', pnl_attr_summary)
    write_csv('outputs/pnl_attribution_component_summary.csv', pnl_attr_components)
    apl_hpl_detail, apl_hpl_summary, apl_hpl_tests, apl_hpl_comparison = apl_hpl_backtesting_proxy(market, window=bt_cfg['window'], alpha=bt_cfg['confidence_level'])
    write_csv('outputs/apl_hpl_backtesting_detail.csv', apl_hpl_detail)
    write_csv('outputs/apl_hpl_backtesting_summary.csv', apl_hpl_summary)
    write_csv('outputs/apl_hpl_backtesting_tests.csv', apl_hpl_tests)
    write_csv('outputs/apl_hpl_backtesting_comparison.csv', apl_hpl_comparison)

    sens = assumption_sensitivity(market['portfolio_pnl'])
    write_csv('outputs/assumption_sensitivity_matrix.csv', sens)

    # False-pass measurement: baseline only checks absolute mc pricing error; final includes asymmetric envelope.
    baseline_pass = benchmark_gated['gate'].eq('PASS')
    risky = asym['asymmetric_status'].eq('BLOCK')
    false_pass_rate = float((baseline_pass & risky).mean())

    # Findings, health, release
    findings = build_findings(
        benchmark_gated, greeks, bt_summary, asym, conv[conv['test']=='mc_convergence'],
        pnl_attr_summary=pnl_attr_summary, modellability_df=modellability, stressed_var_df=stressed_var,
        subportfolio_summary=sub_bt_summary, apl_hpl_comparison=apl_hpl_comparison,
        es_tail_diagnostics_df=es_tail, stress_scenario_coverage_df=scenario_coverage
    )
    write_csv('outputs/model_risk_findings.csv', findings)
    health = build_validation_health_score(findings)
    write_csv('outputs/validation_health_scores.csv', health)
    decision = release_decision(health['validation_health_score'].iloc[0], findings, false_pass_rate=false_pass_rate)
    write_json('outputs/release_decision.json', decision)
    baseline_final = build_baseline_vs_final_summary(benchmark_gated, asym, findings, decision)
    write_csv('outputs/baseline_vs_final_validation_summary.csv', baseline_final)
    regulatory_map = regulatory_mapping_table()
    write_csv('outputs/regulatory_mapping_table.csv', regulatory_map)
    structure_req, non_github = structure_audit(project_path())
    write_csv('outputs/github_runnable_structure_audit.csv', structure_req)
    write_csv('outputs/non_github_artifacts.csv', non_github)
    artifact_idx = artifact_manifest(project_path())
    write_csv('outputs/artifact_manifest.csv', artifact_idx)
    write_json('outputs/run_manifest.json', run_manifest(project_path(), decision))

    # Reports
    write_md('reports/model_card.md', model_card_text())
    write_md('reports/known_limitations.md', limitations_text())
    write_md('reports/compensating_controls.md', controls_text())
    write_md('reports/public_market_data_validation_report.md', make_report('Public Market Data Validation Report', [
        ('Purpose', 'Validates public-data-shaped Federal Reserve H.15 Treasury-rate and FRED ICE BofA OAS sample files used for rates/spread sanity checks.'),
        ('Series-level checks', public_checks.to_markdown(index=False)),
        ('Risk-factor shock summary', public_summary.to_markdown(index=False)),
        ('Correlation matrix', public_corr.to_markdown(index=False)),
        ('FRTB-inspired data-sufficiency proxy', modellability.to_markdown(index=False)),
        ('Claim boundary', 'Sample/fallback public-data mode only; no live proprietary market data or trading-book positions.'),
    ]))
    write_md('reports/regulatory_mapping_memo.md', make_report('Regulatory Mapping Memo', [
        ('Purpose', 'Maps market-risk/model-validation concepts to implemented project artifacts without claiming regulatory compliance.'),
        ('Mapping table', regulatory_map.to_markdown(index=False)),
    ]))
    write_md('reports/resume_metrics_report.md', make_report('Resume Metrics Report', [
        ('Baseline vs final validation summary', baseline_final.to_markdown(index=False)),
        ('Recommended phrasing', 'Use false-pass reduction, subportfolio backtesting, regulatory-style mapping, and public-data sample validation as evidence. Do not claim production trading-desk or regulatory-capital use.'),
    ]))
    write_md('reports/model_scope_and_use_case.md', make_report('Model Scope and Use Case', [
        ('Scope', 'Independent validation of pricing, rates, Monte Carlo simulation, VaR/ES, backtesting, and numerical reliability.'),
        ('Data boundary', 'Synthetic portfolios and public-data-shaped sample files only. No proprietary bank data.'),
        ('Public-data sample mode', 'Federal Reserve H.15-style Treasury rates and FRED ICE BofA OAS-style spread samples are validated for missing/stale/outlier observations and risk-factor shocks.'),
        ('Model inventory', inventory.to_markdown(index=False)),
    ]))
    write_md('reports/pricing_validation_report.md', make_report('Pricing Validation Report', [
        ('Benchmark summary', benchmark_gated[['abs_error','rel_abs_error','gate']].describe(include='all').to_markdown()),
        ('No-arbitrage checks', noarb.to_markdown(index=False)),
        ('Residual error correction', residual_summary.to_markdown(index=False)),
    ]))
    write_md('reports/numerical_reliability_report.md', make_report('Numerical Reliability Report', [
        ('Convergence summary', conv.to_markdown(index=False)),
        ('Seed stability', seed_stability.head().to_markdown(index=False)),
        ('CPU/GPU consistency boundary', cpu_gpu.to_markdown(index=False)),
    ]))
    write_md('reports/var_es_backtesting_report.md', make_report('VaR and ES Backtesting Report', [
        ('VaR/ES results', var_es.to_markdown(index=False)),
        ('Stressed-window VaR proxy', stressed_var.to_markdown(index=False)),
        ('ES tail diagnostics', es_tail.to_markdown(index=False)),
        ('Liquidity-horizon ES proxy', liquidity_es.to_markdown(index=False)),
        ('Backtesting summary', bt_summary.to_markdown(index=False)),
        ('Kupiec/Christoffersen', kc.to_markdown(index=False)),
        ('Subportfolio backtesting summary', sub_bt_summary.to_markdown(index=False)),
        ('Subportfolio statistical tests', sub_bt_tests.to_markdown(index=False)),
        ('P&L attribution proxy summary', pnl_attr_summary.to_markdown(index=False)),
        ('APL/HPL backtesting proxy comparison', apl_hpl_comparison.to_markdown(index=False)),
        ('APL/HPL backtesting summary', apl_hpl_summary.to_markdown(index=False)),
        ('P&L attribution component summary', pnl_attr_components.to_markdown(index=False)),
    ]))
    write_md('reports/stress_testing_report.md', make_report('Stress Testing Report', [
        ('Stress loss by scenario', stress.to_markdown(index=False)),
        ('Stress scenario coverage and monotonicity checks', scenario_coverage.to_markdown(index=False)),
    ]))
    write_md('reports/assumption_impact_report.md', make_report('Assumption Impact Report', [('Assumption sensitivity', sens.to_markdown(index=False))]))
    write_md('reports/validation_health_report.md', make_report('Validation Health Report', [
        ('Health score', health.to_markdown(index=False)),
        ('False-pass rate', false_pass_rate),
        ('Baseline vs final validation summary', baseline_final.to_markdown(index=False)),
        ('ES tail diagnostics', es_tail.to_markdown(index=False)),
        ('APL/HPL proxy comparison', apl_hpl_comparison.to_markdown(index=False)),
        ('Asymmetric envelope status counts', asym['asymmetric_status'].value_counts().to_markdown()),
    ]))
    write_md('reports/model_risk_validation_memo.md', make_report('Model Risk Validation Memo', [
        ('Executive finding', f"Release decision: {decision['release_decision']} with validation health score {decision['validation_health_score']:.1f}."),
        ('Model-risk findings', findings.to_markdown(index=False)),
        ('Claim boundary', decision['claim_boundary']),
        ('Compensating controls', 'Benchmark comparison, numerical tolerance gates, asymmetric validation envelope, stressed-window VaR proxy, P&L attribution proxy, and release gate are required before use.'),
    ]))
    write_md('reports/github_runnable_audit.md', make_report('Local and GitHub Runnable Audit', [
        ('Required structure', structure_req.to_markdown(index=False)),
        ('Non-GitHub artifacts detected', non_github.to_markdown(index=False) if len(non_github) else 'None detected.'),
        ('Artifact manifest sample', artifact_idx.head(20).to_markdown(index=False)),
        ('Local run commands', '`python scripts/run_pipeline.py`, `pytest -q`, `make run`, `make test`.'),
        ('CI recommendation', 'GitHub Actions workflow included under `.github/workflows/ci.yml`; outputs/reports can be regenerated locally.'),
    ]))
    write_md('reports/executive_summary.md', make_report('Executive Summary', [
        ('Purpose', 'This offline framework validates pricing/rates/risk models using benchmark comparison, backtesting, numerical reliability checks, and model-risk governance artifacts.'),
        ('Final decision', decision),
        ('Key metrics', f"Historical VaR99={hvar:,.2f}; Historical ES99={hes:,.2f}; stressed VaR multiplier={float(stressed_var['stressed_var_multiplier'].iloc[0]):.2f}; PLA proxy correlation={float(pnl_attr_summary['pla_proxy_correlation'].iloc[0]):.3f}; APL/HPL corr={float(apl_hpl_comparison['apl_hpl_correlation'].iloc[0]):.3f}; LH-ES component sum={float(liquidity_es['component_scaled_es_sum_proxy'].iloc[0]):,.2f}; baseline false-pass rate={false_pass_rate:.3f}; relative false-pass reduction={float(baseline_final.loc[baseline_final['metric']=='relative_false_pass_reduction','value'].iloc[0]):.1%}; release={decision['release_decision']}."),
        ('Safe resume wording', 'Independent Python quant model validation framework with derivatives, rates, Monte Carlo, VaR/ES, backtesting, numerical reliability, validation memos, and synthetic/public-data claim boundaries.'),
    ]))

    print('Pipeline completed.')
    print(f"Release decision: {decision['release_decision']}")
    print(f"Validation health score: {decision['validation_health_score']:.1f}")
    print(f"False-pass rate: {false_pass_rate:.3f}")


if __name__ == '__main__':
    main()
