import numpy as np
import pandas as pd

from risk.portfolio_var import rolling_backtest_var
from validation.exception_analysis import summarize_exceptions
from validation.kupiec_test import kupiec_pof_test
from validation.christoffersen_test import christoffersen_independence_test


def build_apl_hpl_proxy(market_df: pd.DataFrame) -> pd.DataFrame:
    """Build actual-P&L and hypothetical/explained-P&L proxies.

    The actual P&L includes the synthetic residual/noise component in ``portfolio_pnl``.
    The hypothetical P&L proxy revalues only the risk-factor explained component used by
    the synthetic portfolio design. This is an educational proxy only, not an official
    FRTB APL/HPL or PLA calculation.
    """
    df = market_df.copy()
    hpl = 1_000_000 * (
        0.65 * df['equity_return'].astype(float)
        - 2.5 * df['rate_change'].astype(float)
        - 1.8 * df['spread_change'].astype(float)
    )
    out = df[['date']].copy()
    out['apl_proxy_pnl'] = df['portfolio_pnl'].astype(float)
    out['hpl_proxy_pnl'] = hpl.astype(float)
    out['residual_proxy_pnl'] = out['apl_proxy_pnl'] - out['hpl_proxy_pnl']
    return out


def apl_hpl_backtesting_proxy(market_df: pd.DataFrame, window: int = 250, alpha: float = 0.99):
    pnl = build_apl_hpl_proxy(market_df)
    detail_frames = []
    summary_rows = []
    test_rows = []
    for col, label in [('apl_proxy_pnl', 'APL_proxy'), ('hpl_proxy_pnl', 'HPL_proxy')]:
        bt = rolling_backtest_var(pnl[col], window=window, alpha=alpha)
        bt.insert(0, 'pnl_type', label)
        detail_frames.append(bt)
        summary = summarize_exceptions(bt)
        summary.insert(0, 'pnl_type', label)
        summary_rows.append(summary)
        kup = kupiec_pof_test(int(bt['exception'].sum()), len(bt), alpha=alpha)
        chr_res = christoffersen_independence_test(bt['exception'].astype(int).to_numpy())
        kup['pnl_type'] = label
        chr_res['pnl_type'] = label
        test_rows.extend([kup, chr_res])

    summary_df = pd.concat(summary_rows, ignore_index=True)
    apl_recent = int(summary_df.loc[summary_df['pnl_type'].eq('APL_proxy'), 'recent_250_exceptions'].iloc[0])
    hpl_recent = int(summary_df.loc[summary_df['pnl_type'].eq('HPL_proxy'), 'recent_250_exceptions'].iloc[0])
    corr = float(np.corrcoef(pnl['apl_proxy_pnl'], pnl['hpl_proxy_pnl'])[0, 1])
    residual_std_share = float(pnl['residual_proxy_pnl'].std(ddof=1) / pnl['apl_proxy_pnl'].std(ddof=1))
    comparison = pd.DataFrame([{
        'apl_recent_250_exceptions': apl_recent,
        'hpl_recent_250_exceptions': hpl_recent,
        'apl_hpl_exception_gap': abs(apl_recent - hpl_recent),
        'apl_hpl_correlation': corr,
        'residual_std_share': residual_std_share,
        'status': 'PASS' if abs(apl_recent - hpl_recent) <= 2 and corr >= 0.90 and residual_std_share <= 0.40 else 'REVIEW',
        'claim_boundary': 'APL/HPL backtesting proxy only; not an official FRTB P&L attribution test'
    }])
    return pd.concat(detail_frames, ignore_index=True), summary_df, pd.DataFrame(test_rows), comparison
