import math
import pandas as pd

from risk.portfolio_var import historical_var_es
from risk.subportfolio_backtesting import build_subportfolio_pnl


def liquidity_horizon_es_proxy(market_df: pd.DataFrame, alpha: float = 0.975) -> pd.DataFrame:
    """FRTB-inspired liquidity-horizon ES scaling proxy.

    Uses synthetic subportfolio P&L proxies and square-root-of-time scaling to show how
    longer liquidity horizons can increase tail-risk diagnostics. This is educational and
    deliberately not a regulatory capital calculation.
    """
    pnl = build_subportfolio_pnl(market_df)
    horizons = {
        'derivatives': 10,
        'rates': 20,
        'spread_proxy': 60,
        'aggregate': 10,
    }
    rows = []
    for subportfolio, horizon in horizons.items():
        col = f'{subportfolio}_pnl'
        if col not in pnl.columns:
            continue
        var, es = historical_var_es(pnl[col], alpha=alpha)
        scaled_es = float(es * math.sqrt(horizon / 10.0))
        rows.append({
            'subportfolio': subportfolio,
            'alpha': alpha,
            'liquidity_horizon_days': horizon,
            'base_10day_es_proxy': float(es),
            'scaled_liquidity_horizon_es_proxy': scaled_es,
            'scaling_multiplier': float(math.sqrt(horizon / 10.0)),
            'claim_boundary': 'FRTB-inspired liquidity-horizon ES proxy; not a regulatory capital calculation'
        })
    df = pd.DataFrame(rows)
    component_sum = float(df.loc[~df['subportfolio'].eq('aggregate'), 'scaled_liquidity_horizon_es_proxy'].sum())
    df['component_scaled_es_sum_proxy'] = component_sum
    df['status'] = 'PASS'
    return df
