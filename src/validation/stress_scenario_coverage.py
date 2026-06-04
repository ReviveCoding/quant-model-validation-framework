import pandas as pd


def stress_scenario_coverage(stress_results: pd.DataFrame, stress_scenarios: list) -> pd.DataFrame:
    scenario_cfg = pd.DataFrame(stress_scenarios)
    merged = stress_results.merge(scenario_cfg, left_on='scenario', right_on='name', how='left').drop(columns=['name'])
    rows = []
    rows.append({'check': 'has_equity_down_scenario', 'value': bool((merged['equity_shock'] < 0).any()), 'status': 'PASS' if (merged['equity_shock'] < 0).any() else 'REVIEW'})
    rows.append({'check': 'has_volatility_up_scenario', 'value': bool((merged['volatility_shock'] > 0).any()), 'status': 'PASS' if (merged['volatility_shock'] > 0).any() else 'REVIEW'})
    rows.append({'check': 'has_rate_up_scenario', 'value': bool((merged['rate_shock'] > 0).any()), 'status': 'PASS' if (merged['rate_shock'] > 0).any() else 'REVIEW'})
    # Monotonicity on the configured equity-down/vol-up ladder.
    s10 = merged.loc[merged['scenario'].eq('equity_down_10_vol_up'), 'stress_loss']
    s25 = merged.loc[merged['scenario'].eq('equity_down_25_vol_spike'), 'stress_loss']
    monotonic = bool(len(s10) and len(s25) and float(s25.iloc[0]) >= float(s10.iloc[0]))
    rows.append({'check': 'equity_vol_ladder_loss_monotonicity', 'value': monotonic, 'status': 'PASS' if monotonic else 'REVIEW'})
    return pd.DataFrame(rows)
