from data.generate_synthetic_market import generate_synthetic_market
from risk.apl_hpl_backtesting import apl_hpl_backtesting_proxy


def test_apl_hpl_backtesting_proxy_runs():
    market = generate_synthetic_market(n_days=800)
    detail, summary, tests, comp = apl_hpl_backtesting_proxy(market)
    assert {'APL_proxy', 'HPL_proxy'} == set(summary['pnl_type'])
    assert comp['apl_hpl_correlation'].iloc[0] > 0.90
    assert comp['status'].iloc[0] in {'PASS', 'REVIEW'}
    assert len(detail) > 0 and len(tests) == 4
