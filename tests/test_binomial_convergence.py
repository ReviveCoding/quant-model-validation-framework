from models.black_scholes import bs_call_price
from models.binomial_tree import binomial_call_price


def test_binomial_converges_near_bs():
    bs = bs_call_price(100, 100, 1, 0.03, 0.25)
    bt = binomial_call_price(100, 100, 1, 0.03, 0.25, steps=400)
    assert abs(bs - bt) < 0.05
