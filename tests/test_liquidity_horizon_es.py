from data.generate_synthetic_market import generate_synthetic_market
from risk.liquidity_horizon_es import liquidity_horizon_es_proxy


def test_liquidity_horizon_es_proxy_runs():
    market = generate_synthetic_market(n_days=800)
    out = liquidity_horizon_es_proxy(market)
    assert {'derivatives', 'rates', 'spread_proxy', 'aggregate'}.issubset(set(out['subportfolio']))
    assert (out['scaled_liquidity_horizon_es_proxy'] > 0).all()
    assert (out['status'] == 'PASS').all()
