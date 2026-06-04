from data.generate_synthetic_market import generate_synthetic_market
from risk.subportfolio_backtesting import build_subportfolio_pnl, subportfolio_backtests


def test_subportfolio_backtesting_outputs():
    market = generate_synthetic_market(n_days=420)
    pnl = build_subportfolio_pnl(market)
    assert {'derivatives_pnl','rates_pnl','spread_proxy_pnl','aggregate_pnl'}.issubset(set(pnl.columns))
    detail, summary, tests = subportfolio_backtests(market, window=250, alpha=0.99)
    assert not detail.empty
    assert not summary.empty
    assert not tests.empty
