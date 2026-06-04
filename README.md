# Quant Model Validation & Numerical Risk Simulation Framework

An offline, end-to-end **independent quant model validation framework** for derivatives, interest-rate models, Monte Carlo risk simulation, VaR/Expected Shortfall backtesting, numerical reliability, and model-risk governance artifacts.

This repository was designed as a non-production portfolio project for market-risk/model-validation roles. It uses synthetic portfolios by default, optional public-data sample files shaped after Federal Reserve H.15 Treasury-rate and FRED ICE BofA OAS-style data, and conservative claim boundaries.

## What this project demonstrates

- Model inventory and validation scope definition
- Black-Scholes, binomial tree, Monte Carlo option pricing, Heston simulation, Vasicek and CIR rate paths
- Independent benchmark comparison, no-arbitrage checks, Greeks validation, finite-difference tolerance tests
- Full-revaluation vs delta-gamma P&L, VaR, Expected Shortfall, stress loss
- 250-day rolling VaR backtesting with Kupiec and Christoffersen tests
- Public-data sample validation for Federal Reserve H.15-style Treasury rates and FRED ICE BofA OAS-style spread factors
- Subportfolio backtesting proxies for derivatives, rates, spread-risk, and aggregate portfolio P&L
- Regulatory-style mapping memo connecting VaR/ES/backtesting/assumption testing artifacts to market-risk model validation concepts
- Stressed-window VaR proxy using maximum rolling historical VaR window selection
- P&L attribution proxy comparing actual vs explained P&L and residual-risk budget

- APL/HPL backtesting proxy comparing actual P&L proxy against hypothetical/explained P&L proxy
- ES tail diagnostics comparing modeled ES to realized average tail losses
- FRTB-inspired liquidity-horizon ES proxy across derivatives, rates, spread-risk, and aggregate P&L proxies
- Stress scenario coverage and monotonicity checks for equity, volatility, and rate shocks
- Artifact manifest and run manifest for reproducibility and GitHub review
- Dockerfile for containerized local validation
- FRTB-inspired risk-factor modellability/data-sufficiency proxy for public-data samples
- Baseline-vs-final validation summary showing one-sided false-pass reduction from the specialty reliability layer
- Numerical reliability: Monte Carlo convergence, seed stability, tolerance gates, optional CPU/GPU consistency scaffold
- Specialty reliability layer: Validation Health Score, closed-form NumPy ridge residual error-correction challenger, asymmetric validation envelope
- Governance artifacts: validation memo, model card, known limitations, compensating controls, model-risk findings, release gate

## Claim boundary

This is an offline/non-production validation framework using synthetic portfolios and public-data samples. It is not a bank trading-desk model, not a regulatory capital model, not FRTB-compliant, and does not use proprietary bank data.

## Run

Recommended Python: **3.11**. The GitHub Actions workflow uses Python 3.11 for reproducible CI validation.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
PYTHONDONTWRITEBYTECODE=1 python scripts/run_pipeline.py
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q
```

Or:

```bash
make validate
```

## Main outputs

After `python scripts/run_pipeline.py`, generated artifacts are saved under `outputs/` and `reports/`.

Key files:

- `outputs/model_inventory.csv`
- `outputs/benchmark_comparison.csv`
- `outputs/greeks_validation.csv`
- `outputs/convergence_summary.csv`
- `outputs/var_es_results.csv`
- `outputs/stress_loss_results.csv`
- `outputs/backtesting_exceptions.csv`
- `outputs/kupiec_christoffersen_results.csv`
- `outputs/assumption_sensitivity_matrix.csv`
- `outputs/validation_health_scores.csv`
- `outputs/model_risk_findings.csv`
- `outputs/baseline_vs_final_validation_summary.csv`
- `outputs/public_market_data_validation.csv`
- `outputs/subportfolio_backtesting_summary.csv`
- `outputs/regulatory_mapping_table.csv`
- `outputs/stressed_var_results.csv`
- `outputs/pnl_attribution_proxy_summary.csv`
- `outputs/apl_hpl_backtesting_comparison.csv`
- `outputs/es_tail_diagnostics.csv`
- `outputs/liquidity_horizon_es_proxy.csv`
- `outputs/stress_scenario_coverage.csv`
- `outputs/artifact_manifest.csv`
- `outputs/run_manifest.json`
- `outputs/risk_factor_modellability_proxy.csv`
- `reports/github_runnable_audit.md`
- `outputs/release_decision.json`
- `reports/public_market_data_validation_report.md`
- `reports/regulatory_mapping_memo.md`
- `reports/resume_metrics_report.md`
- `reports/model_risk_validation_memo.md`
- `reports/executive_summary.md`


## Optional dashboard

The dashboard dependencies are kept separate from the core validation dependencies so GitHub Actions and Docker validation stay lightweight.

```bash
pip install -r requirements-dashboard.txt
streamlit run src/dashboard/streamlit_app.py
```

## Docker run

```bash
docker build -t qmv-framework .
docker run --rm qmv-framework
```

## Resume-safe framing

> Built an independent Python quant model validation framework for derivative pricing, interest-rate models, and market-risk simulation, covering Black-Scholes, binomial tree, Monte Carlo, Heston, Vasicek/CIR rates, no-arbitrage checks, Greeks validation, full-revaluation vs delta-gamma P&L, VaR/Expected Shortfall, stress diagnostics, and Kupiec/Christoffersen backtesting.

> Added numerical-reliability and model-risk controls including public-data sample validation, subportfolio VaR backtesting, Monte Carlo convergence diagnostics, finite-difference tolerance gates, seed-stability tests, asymmetric validation envelopes, residual error-correction challengers, regulatory-style mapping, finding severity, validation memos, model cards, known limitations, and conservative synthetic/public-data claim boundaries.
