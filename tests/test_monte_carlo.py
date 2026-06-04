from models.black_scholes import bs_call_price
from models.monte_carlo_option import mc_call_price


def test_monte_carlo_confidence_reasonable():
    bs = bs_call_price(100, 100, 1, 0.03, 0.25)
    mc, se = mc_call_price(100, 100, 1, 0.03, 0.25, paths=30000, seed=42)
    assert abs(mc - bs) < 4 * se
