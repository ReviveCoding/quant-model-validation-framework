from models.black_scholes import bs_call_greeks
from benchmarks.finite_difference_checks import finite_diff_delta, finite_diff_gamma


def test_finite_difference_greeks():
    g = bs_call_greeks(100, 100, 1, 0.03, 0.25)
    assert abs(g['delta'] - finite_diff_delta(100,100,1,0.03,0.25)) < 1e-3
    assert abs(g['gamma'] - finite_diff_gamma(100,100,1,0.03,0.25)) < 1e-3
