import numpy as np


def heston_call_price(S, K, T, r, v0, kappa=2.0, theta=0.04, xi=0.35, rho=-0.55, paths=8000, steps=80, seed=17):
    rng = np.random.default_rng(seed)
    dt = T / steps
    S_paths = np.full(paths, S, dtype=float)
    v = np.full(paths, max(v0, 1e-6), dtype=float)
    for _ in range(steps):
        z1 = rng.standard_normal(paths)
        z2 = rho * z1 + np.sqrt(max(1-rho**2, 0)) * rng.standard_normal(paths)
        v = np.maximum(v + kappa*(theta-v)*dt + xi*np.sqrt(np.maximum(v,0))*np.sqrt(dt)*z2, 1e-8)
        S_paths = S_paths * np.exp((r - 0.5*v)*dt + np.sqrt(v*dt)*z1)
    payoff = np.maximum(S_paths - K, 0.0)
    return float(np.exp(-r*T) * payoff.mean())
