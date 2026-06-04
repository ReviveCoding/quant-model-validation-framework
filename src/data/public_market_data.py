from pathlib import Path
import numpy as np
import pandas as pd


def _safe_pct_change(s: pd.Series) -> pd.Series:
    return s.astype(float).diff()


def validate_public_market_data(data_dir: Path):
    """Validate public-data-shaped H.15 and FRED OAS sample files.

    The project remains runnable without internet access. These files are shaped after
    Federal Reserve H.15 Treasury constant maturity data and FRED ICE BofA OAS series,
    but are sample/fallback data, not live market downloads.
    """
    rates_path = Path(data_dir) / 'h15_rates_sample.csv'
    oas_path = Path(data_dir) / 'fred_oas_sample.csv'
    rates = pd.read_csv(rates_path, parse_dates=['date'])
    oas = pd.read_csv(oas_path, parse_dates=['date'])
    panel = rates.merge(oas, on='date', how='outer').sort_values('date').reset_index(drop=True)

    numeric_cols = [c for c in panel.columns if c != 'date']
    checks = []
    shock_df = panel[['date']].copy()
    for col in numeric_cols:
        s = panel[col].astype(float)
        shock = _safe_pct_change(s)
        shock_df[f'{col}_shock'] = shock
        stale = s.diff().fillna(0).abs().eq(0)
        # robust z-score for outlier shocks
        med = shock.median(skipna=True)
        mad = (shock - med).abs().median(skipna=True)
        denom = 1.4826 * mad if mad and mad > 0 else shock.std(ddof=1)
        z = ((shock - med).abs() / denom).replace([np.inf, -np.inf], np.nan) if denom and denom > 0 else shock * 0
        checks.append({
            'series': col,
            'observations': int(s.notna().sum()),
            'missing_count': int(s.isna().sum()),
            'missing_share': float(s.isna().mean()),
            'stale_count': int(stale.iloc[1:].sum()),
            'outlier_shock_count': int((z > 6).sum(skipna=True)),
            'min_value': float(s.min()),
            'max_value': float(s.max()),
            'mean_daily_abs_shock': float(shock.abs().mean(skipna=True)),
            'status': 'PASS' if s.isna().mean() <= 0.02 else 'REVIEW',
        })

    shock_cols = [c for c in shock_df.columns if c.endswith('_shock')]
    factor_panel = panel.merge(shock_df[['date'] + shock_cols], on='date', how='left')

    summary_rows = []
    for col in shock_cols:
        x = factor_panel[col].dropna()
        summary_rows.append({
            'risk_factor': col,
            'mean_shock': float(x.mean()) if len(x) else 0.0,
            'volatility': float(x.std(ddof=1)) if len(x) > 1 else 0.0,
            'p01_shock': float(x.quantile(0.01)) if len(x) else 0.0,
            'p99_shock': float(x.quantile(0.99)) if len(x) else 0.0,
        })

    corr = factor_panel[shock_cols].corr().reset_index().rename(columns={'index': 'risk_factor'}) if shock_cols else pd.DataFrame()
    return pd.DataFrame(checks), pd.DataFrame(summary_rows), factor_panel, corr
