from data.generate_synthetic_market import generate_synthetic_market
from risk.pnl_attribution import pnl_attribution_proxy


def test_pnl_attribution_proxy_quality_metrics():
    market = generate_synthetic_market(n_days=350)
    detail, summary, components = pnl_attribution_proxy(market)
    assert len(detail) == len(market)
    assert summary['pla_proxy_correlation'].iloc[0] > 0.5
    assert summary['unexplained_share'].iloc[0] >= 0
    assert set(['equity_component','rates_component','spread_component']).issubset(set(components['component']))
