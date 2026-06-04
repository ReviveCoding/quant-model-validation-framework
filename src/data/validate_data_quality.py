import pandas as pd


def validate_time_series(df: pd.DataFrame, date_col='date') -> pd.DataFrame:
    checks = []
    checks.append({'check': 'row_count', 'value': len(df), 'status': 'PASS' if len(df) > 250 else 'REVIEW'})
    checks.append({'check': 'duplicate_dates', 'value': int(df[date_col].duplicated().sum()), 'status': 'PASS' if df[date_col].duplicated().sum() == 0 else 'REVIEW'})
    missing = int(df.isna().sum().sum())
    checks.append({'check': 'missing_values_total', 'value': missing, 'status': 'PASS' if missing == 0 else 'REVIEW'})
    numeric = df.select_dtypes('number')
    if not numeric.empty:
        stale = int((numeric.diff().abs() < 1e-12).sum().sum())
        checks.append({'check': 'stale_observations_proxy', 'value': stale, 'status': 'PASS' if stale < len(df) else 'REVIEW'})
        outliers = int(((numeric - numeric.mean()).abs() > 6 * numeric.std(ddof=0)).sum().sum())
        checks.append({'check': 'six_sigma_outliers', 'value': outliers, 'status': 'PASS' if outliers == 0 else 'REVIEW'})
    return pd.DataFrame(checks)
