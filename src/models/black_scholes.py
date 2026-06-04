import numpy as np
from scipy.stats import norm


def d1(S, K, T, r, sigma):
    S = np.asarray(S, dtype=float)
    return (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))


def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


def bs_call_price(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = D1 - sigma * np.sqrt(T)
    return S * norm.cdf(D1) - K * np.exp(-r * T) * norm.cdf(D2)


def bs_call_greeks(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    D2 = D1 - sigma * np.sqrt(T)
    delta = norm.cdf(D1)
    gamma = norm.pdf(D1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(D1) * np.sqrt(T)
    theta = -(S * norm.pdf(D1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * norm.cdf(D2)
    rho = K * T * np.exp(-r*T) * norm.cdf(D2)
    return {'delta': delta, 'gamma': gamma, 'vega': vega, 'theta': theta, 'rho': rho}
