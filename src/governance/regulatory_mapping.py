import pandas as pd


def regulatory_mapping_table() -> pd.DataFrame:
    rows = [
        {
            'requirement_or_concept': '250-business-day VaR backtesting',
            'project_artifact': 'outputs/backtesting_exceptions.csv; outputs/subportfolio_backtesting_summary.csv',
            'implementation': 'Rolling one-day VaR backtesting with exception counts and severity by aggregate and subportfolio proxy.',
            'claim_boundary': 'Regulatory-style diagnostic only; not a bank capital model.'
        },
        {
            'requirement_or_concept': '99% one-tail VaR',
            'project_artifact': 'outputs/var_es_results.csv',
            'implementation': 'Historical, normal Monte Carlo, and Student-t Monte Carlo VaR99/ES99 estimates.',
            'claim_boundary': 'Synthetic portfolio and sample public-data mode.'
        },
        {
            'requirement_or_concept': 'Expected Shortfall / FRTB-inspired tail-risk diagnostics',
            'project_artifact': 'outputs/var_es_results.csv; reports/assumption_impact_report.md',
            'implementation': 'ES99 and heavy-tail sensitivity to show tail-risk behavior beyond VaR.',
            'claim_boundary': 'FRTB-inspired; not FRTB-compliant.'
        },
        {
            'requirement_or_concept': 'Alternative modeling assumptions',
            'project_artifact': 'outputs/assumption_sensitivity_matrix.csv',
            'implementation': 'Historical vs Monte Carlo, normal vs Student-t, and volatility scaling comparisons.',
            'claim_boundary': 'Model-development benchmark evidence, not production validation.'
        },
        {
            'requirement_or_concept': 'Model limitations and compensating controls',
            'project_artifact': 'reports/known_limitations.md; reports/compensating_controls.md',
            'implementation': 'Explicit documentation of synthetic data, model-use limits, challenger checks, and release gates.',
            'claim_boundary': 'Non-production portfolio project.'
        },
    ]
    return pd.DataFrame(rows)
