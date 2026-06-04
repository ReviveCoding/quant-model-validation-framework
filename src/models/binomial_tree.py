import numpy as np


def binomial_call_price(S, K, T, r, sigma, steps=200):
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    # vectorized terminal prices
    j = np.arange(steps + 1)
    ST = S * (u ** j) * (d ** (steps - j))
    values = np.maximum(ST - K, 0.0)
    disc = np.exp(-r * dt)
    for _ in range(steps):
        values = disc * (p * values[1:] + (1-p) * values[:-1])
    return float(values[0])
