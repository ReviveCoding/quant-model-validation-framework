from models.black_scholes import bs_call_price, bs_call_greeks


def full_revaluation_change(S, K, T, r, sigma, dS):
    return bs_call_price(S+dS, K, T, r, sigma) - bs_call_price(S, K, T, r, sigma)


def delta_gamma_change(S, K, T, r, sigma, dS):
    g = bs_call_greeks(S, K, T, r, sigma)
    return g['delta'] * dS + 0.5 * g['gamma'] * dS * dS
