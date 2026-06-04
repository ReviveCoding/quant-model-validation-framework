import numpy as np
import pandas as pd
from pathlib import Path


def generate_synthetic_market(n_days=800, seed=42):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range('2021-01-04', periods=n_days)
    # Simple correlated market factors: equity, rate, spread, vol.
    corr = np.array([
        [1.00, -0.25, -0.45, -0.60],
        [-0.25, 1.00, 0.30, 0.20],
        [-0.45, 0.30, 1.00, 0.55],
        [-0.60, 0.20, 0.55, 1.00],
    ])
    vols = np.array([0.012, 0.0007, 0.0018, 0.006])
    cov = corr * np.outer(vols, vols)
    shocks = rng.multivariate_normal(np.zeros(4), cov, size=n_days)
    df = pd.DataFrame(shocks, columns=['equity_return', 'rate_change', 'spread_change', 'vol_change'])
    df.insert(0, 'date', dates)
    df['spot_index'] = 100 * np.exp(np.cumsum(df['equity_return']))
    df['rate_2y'] = np.clip(0.035 + np.cumsum(df['rate_change']), 0.001, 0.12)
    df['oas_ig'] = np.clip(0.012 + np.cumsum(df['spread_change']), 0.002, 0.08)
    df['implied_vol'] = np.clip(0.22 + np.cumsum(df['vol_change']), 0.08, 0.85)
    df['portfolio_return'] = 0.65 * df['equity_return'] - 2.5 * df['rate_change'] - 1.8 * df['spread_change'] + rng.normal(0, 0.004, n_days)
    df['portfolio_pnl'] = 1_000_000 * df['portfolio_return']
    return df


def generate_option_portfolio(n_options=240, seed=123):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        'option_id': [f'OPT_{i:04d}' for i in range(n_options)],
        'S': rng.uniform(70, 130, n_options),
        'K': rng.uniform(75, 125, n_options),
        'T': rng.uniform(0.08, 2.0, n_options),
        'r': rng.uniform(0.01, 0.06, n_options),
        'sigma': rng.uniform(0.12, 0.55, n_options),
        'position': rng.integers(-50, 75, n_options),
    })
    df['option_type'] = 'call'
    return df


def create_public_sample_files(data_dir: Path):
    data_dir.mkdir(parents=True, exist_ok=True)
    dates = pd.bdate_range('2023-01-02', periods=260)
    rng = np.random.default_rng(77)
    rates = pd.DataFrame({
        'date': dates,
        'DGS2': 0.035 + np.cumsum(rng.normal(0, 0.00035, len(dates))),
        'DGS10': 0.038 + np.cumsum(rng.normal(0, 0.00030, len(dates))),
    })
    oas = pd.DataFrame({
        'date': dates,
        'BAMLC0A0CM': 0.012 + np.cumsum(rng.normal(0, 0.00025, len(dates))),
        'BAMLH0A0HYM2': 0.036 + np.cumsum(rng.normal(0, 0.00070, len(dates))),
    })
    rates.to_csv(data_dir / 'h15_rates_sample.csv', index=False)
    oas.to_csv(data_dir / 'fred_oas_sample.csv', index=False)
    return rates, oas
