import numpy as np


def vasicek_paths(r0=0.035, kappa=0.8, theta=0.04, sigma=0.015, T=1.0, steps=252, paths=5000, seed=5):
    rng = np.random.default_rng(seed)
    dt = T/steps
    r = np.full((paths, steps+1), r0, dtype=float)
    for t in range(steps):
        r[:, t+1] = r[:, t] + kappa*(theta-r[:, t])*dt + sigma*np.sqrt(dt)*rng.standard_normal(paths)
    return r


def cir_paths(r0=0.035, kappa=0.8, theta=0.04, sigma=0.08, T=1.0, steps=252, paths=5000, seed=6):
    rng = np.random.default_rng(seed)
    dt = T/steps
    r = np.full((paths, steps+1), r0, dtype=float)
    for t in range(steps):
        r[:, t+1] = np.maximum(r[:, t] + kappa*(theta-r[:, t])*dt + sigma*np.sqrt(np.maximum(r[:, t],0))*np.sqrt(dt)*rng.standard_normal(paths), 0.0)
    return r
