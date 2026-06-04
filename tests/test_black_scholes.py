from models.black_scholes import bs_call_price, bs_call_greeks


def test_black_scholes_price_positive():
    px = bs_call_price(100, 100, 1, 0.03, 0.25)
    assert px > 0
    assert px < 100


def test_delta_range():
    g = bs_call_greeks(100, 100, 1, 0.03, 0.25)
    assert 0 < g['delta'] < 1
    assert g['gamma'] > 0
