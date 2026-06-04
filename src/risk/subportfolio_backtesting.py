import pandas as pd
from risk.portfolio_var import rolling_backtest_var
from validation.kupiec_test import kupiec_pof_test
from validation.christoffersen_test import christoffersen_independence_test
from validation.exception_analysis import summarize_exceptions


def build_subportfolio_pnl(market: pd.DataFrame) -> pd.DataFrame:
    """Create transparent synthetic subportfolio P&L proxies from market factors."""
    out = market[['date']].copy()
    out['derivatives_pnl'] = 1_000_000 * (0.50 * market['equity_return'] + 0.80 * market['vol_change'])
    out['rates_pnl'] = 1_000_000 * (-3.20 * market['rate_change'])
    out['spread_proxy_pnl'] = 1_000_000 * (-2.40 * market['spread_change'] + 0.15 * market['equity_return'])
    out['aggregate_pnl'] = market['portfolio_pnl']
    return out


def subportfolio_backtests(market: pd.DataFrame, window=250, alpha=0.99):
    pnl = build_subportfolio_pnl(market)
    detail_frames = []
    summary_rows = []
    test_rows = []
    for col in [c for c in pnl.columns if c.endswith('_pnl')]:
        bt = rolling_backtest_var(pnl[col], window=window, alpha=alpha)
        bt.insert(0, 'subportfolio', col.replace('_pnl', ''))
        detail_frames.append(bt)
        summary = summarize_exceptions(bt)
        summary.insert(0, 'subportfolio', col.replace('_pnl', ''))
        summary_rows.append(summary)
        kup = kupiec_pof_test(int(bt['exception'].sum()), len(bt), alpha=alpha)
        chr_res = christoffersen_independence_test(bt['exception'].astype(int).to_numpy())
        kup['subportfolio'] = col.replace('_pnl', '')
        chr_res['subportfolio'] = col.replace('_pnl', '')
        test_rows.extend([kup, chr_res])
    return pd.concat(detail_frames, ignore_index=True), pd.concat(summary_rows, ignore_index=True), pd.DataFrame(test_rows)
