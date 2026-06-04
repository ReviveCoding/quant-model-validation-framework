from models.black_scholes import bs_call_price


def finite_diff_delta(S, K, T, r, sigma, h=1e-3):
    return (bs_call_price(S+h, K, T, r, sigma) - bs_call_price(S-h, K, T, r, sigma)) / (2*h)


def finite_diff_gamma(S, K, T, r, sigma, h=1e-2):
    return (bs_call_price(S+h, K, T, r, sigma) - 2*bs_call_price(S, K, T, r, sigma) + bs_call_price(S-h, K, T, r, sigma)) / (h*h)
