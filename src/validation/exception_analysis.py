import pandas as pd


def _traffic_light(exceptions: int):
    if exceptions <= 4:
        return 'GREEN'
    if exceptions <= 9:
        return 'YELLOW'
    return 'RED'


def summarize_exceptions(backtest_df):
    """Summarize VaR exceptions.

    For regulatory-style display, the traffic-light zone is based on the most recent
    250 backtest observations when more than 250 observations are available. The full
    sample count is still reported as an additional outcomes-analysis diagnostic.
    """
    n = len(backtest_df)
    exceptions = int(backtest_df['exception'].sum()) if n else 0
    severity_sum = float(backtest_df['exception_severity'].sum()) if n else 0.0
    recent = backtest_df.tail(min(250, n)) if n else backtest_df
    recent_n = len(recent)
    recent_exceptions = int(recent['exception'].sum()) if recent_n else 0
    recent_severity = float(recent['exception_severity'].sum()) if recent_n else 0.0
    zone = _traffic_light(recent_exceptions)
    return pd.DataFrame([{
        'n_obs': n,
        'exceptions': exceptions,
        'exception_rate': exceptions / max(n, 1),
        'severity_sum': severity_sum,
        'recent_250_obs': recent_n,
        'recent_250_exceptions': recent_exceptions,
        'recent_250_exception_rate': recent_exceptions / max(recent_n, 1),
        'recent_250_severity_sum': recent_severity,
        'traffic_light_zone': zone,
        'traffic_light_basis': 'most_recent_250_observations' if n > 250 else 'available_observations'
    }])
