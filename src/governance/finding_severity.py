import pandas as pd


def build_findings(benchmark_df, greeks_df, backtest_summary, asym_df, convergence_df,
                   pnl_attr_summary=None, modellability_df=None, stressed_var_df=None, subportfolio_summary=None,
                   apl_hpl_comparison=None, es_tail_diagnostics_df=None, stress_scenario_coverage_df=None):
    rows = []
    if (benchmark_df['gate'] == 'BLOCK').any():
        rows.append({'finding_id': 'F001', 'area': 'pricing', 'severity': 'CRITICAL', 'description': 'Benchmark pricing error breached block threshold.', 'recommendation': 'Require model recalibration or challenger review.'})
    if (greeks_df['status'] == 'REVIEW').mean() > 0.10:
        rows.append({'finding_id': 'F002', 'area': 'greeks', 'severity': 'HIGH', 'description': 'Greek finite-difference validation produced elevated review rate.', 'recommendation': 'Review finite-difference step and analytic formulas.'})
    zone = backtest_summary.iloc[0]['traffic_light_zone']
    if zone == 'RED':
        rows.append({'finding_id': 'F003', 'area': 'backtesting', 'severity': 'CRITICAL', 'description': 'VaR backtesting is in red traffic-light zone.', 'recommendation': 'Block release and review VaR assumptions.'})
    elif zone == 'YELLOW':
        rows.append({'finding_id': 'F003', 'area': 'backtesting', 'severity': 'HIGH', 'description': 'VaR backtesting is in yellow traffic-light zone.', 'recommendation': 'Escalate for model-risk review.'})
    if (asym_df['asymmetric_status'] == 'BLOCK').mean() > 0.05:
        rows.append({'finding_id': 'F004', 'area': 'asymmetric_envelope', 'severity': 'HIGH', 'description': 'Asymmetric validation found risky underestimation errors.', 'recommendation': 'Require compensating controls for underestimation risk.'})
    if convergence_df['abs_error'].tail(1).iloc[0] > convergence_df['abs_error'].head(1).iloc[0]:
        rows.append({'finding_id': 'F005', 'area': 'numerical_convergence', 'severity': 'MEDIUM', 'description': 'Monte Carlo convergence did not improve in final grid point.', 'recommendation': 'Increase path count or investigate variance reduction.'})
    if pnl_attr_summary is not None and len(pnl_attr_summary):
        if str(pnl_attr_summary.iloc[0].get('status', 'PASS')) != 'PASS':
            rows.append({'finding_id': 'F006', 'area': 'pnl_attribution_proxy', 'severity': 'MEDIUM', 'description': 'Actual-vs-explained P&L attribution proxy did not meet correlation or unexplained-share thresholds.', 'recommendation': 'Review omitted risk factors, basis effects, and residual P&L drivers.'})
    if modellability_df is not None and len(modellability_df):
        if (modellability_df['status'] != 'PASS').any():
            rows.append({'finding_id': 'F007', 'area': 'risk_factor_modellability_proxy', 'severity': 'MEDIUM', 'description': 'One or more public-data sample risk factors failed the data-sufficiency proxy.', 'recommendation': 'Increase observation count, reduce stale quotes, or apply non-modellable-risk-factor controls.'})

    if subportfolio_summary is not None and len(subportfolio_summary):
        yellow = subportfolio_summary[subportfolio_summary['traffic_light_zone'].eq('YELLOW')]
        red = subportfolio_summary[subportfolio_summary['traffic_light_zone'].eq('RED')]
        if len(red):
            rows.append({'finding_id': 'F009', 'area': 'subportfolio_backtesting', 'severity': 'HIGH', 'description': f"{len(red)} subportfolio backtesting proxy segment(s) are in red traffic-light zone.", 'recommendation': 'Escalate subportfolio VaR assumptions and risk-factor mapping.'})
        elif len(yellow):
            rows.append({'finding_id': 'F009', 'area': 'subportfolio_backtesting', 'severity': 'MEDIUM', 'description': f"{len(yellow)} subportfolio backtesting proxy segment(s) are in yellow traffic-light zone.", 'recommendation': 'Monitor subportfolio exceptions and document risk-factor-specific limitations.'})

    if stressed_var_df is not None and len(stressed_var_df):
        multiplier = float(stressed_var_df.iloc[0].get('stressed_var_multiplier', 1.0))
        if multiplier > 1.50:
            rows.append({'finding_id': 'F008', 'area': 'stressed_var_proxy', 'severity': 'HIGH', 'description': 'Stressed-window VaR materially exceeds full-sample VaR.', 'recommendation': 'Escalate stress-window selection, scenario design, and tail-risk capital buffer assumptions.'})
        elif multiplier > 1.25:
            rows.append({'finding_id': 'F008', 'area': 'stressed_var_proxy', 'severity': 'MEDIUM', 'description': 'Stressed-window VaR exceeds full-sample VaR.', 'recommendation': 'Document stress-window sensitivity and require stress-specific monitoring.'})

    if apl_hpl_comparison is not None and len(apl_hpl_comparison):
        if str(apl_hpl_comparison.iloc[0].get('status', 'PASS')) != 'PASS':
            rows.append({'finding_id': 'F010', 'area': 'apl_hpl_backtesting_proxy', 'severity': 'MEDIUM', 'description': 'APL/HPL proxy comparison exceeded exception-gap, correlation, or residual-share thresholds.', 'recommendation': 'Review unexplained P&L drivers and document APL/HPL proxy limitations.'})

    if es_tail_diagnostics_df is not None and len(es_tail_diagnostics_df):
        review_rows = es_tail_diagnostics_df[es_tail_diagnostics_df['status'].ne('PASS')]
        if len(review_rows):
            rows.append({'finding_id': 'F011', 'area': 'es_tail_diagnostics', 'severity': 'MEDIUM', 'description': f'{len(review_rows)} ES tail diagnostic method(s) failed realized-tail conservatism checks.', 'recommendation': 'Review tail distribution assumptions and ES calibration.'})

    if stress_scenario_coverage_df is not None and len(stress_scenario_coverage_df):
        review_rows = stress_scenario_coverage_df[stress_scenario_coverage_df['status'].ne('PASS')]
        if len(review_rows):
            rows.append({'finding_id': 'F012', 'area': 'stress_scenario_coverage', 'severity': 'MEDIUM', 'description': f'{len(review_rows)} stress scenario coverage or monotonicity check(s) require review.', 'recommendation': 'Expand scenario library and retest monotonic stress severity.'})

    if not rows:
        rows.append({'finding_id': 'F000', 'area': 'overall', 'severity': 'LOW', 'description': 'No critical validation issue detected in offline benchmark run.', 'recommendation': 'Keep monitoring assumptions and claim boundaries.'})
    return pd.DataFrame(rows)
