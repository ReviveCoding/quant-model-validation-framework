import numpy as np


def mc_call_price(S, K, T, r, sigma, paths=20000, seed=7):
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(paths)
    ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * z)
    payoffs = np.maximum(ST - K, 0.0)
    disc = np.exp(-r * T)
    price = disc * np.mean(payoffs)
    stderr = disc * np.std(payoffs, ddof=1) / np.sqrt(paths)
    return float(price), float(stderr)
