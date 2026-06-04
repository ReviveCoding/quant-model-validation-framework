import pandas as pd
from models.black_scholes import bs_call_price
from models.binomial_tree import binomial_call_price
from models.monte_carlo_option import mc_call_price


def binomial_convergence_case(S=100, K=100, T=1.0, r=0.03, sigma=0.25):
    bs = bs_call_price(S, K, T, r, sigma)
    rows = []
    for steps in [25, 50, 100, 200, 400]:
        px = binomial_call_price(S, K, T, r, sigma, steps=steps)
        rows.append({'test': 'binomial_convergence', 'grid': steps, 'price': px, 'benchmark': bs, 'abs_error': abs(px-bs)})
    return pd.DataFrame(rows)


def monte_carlo_convergence_case(S=100, K=100, T=1.0, r=0.03, sigma=0.25, seed=7):
    bs = bs_call_price(S, K, T, r, sigma)
    rows = []
    for paths in [1000, 2500, 5000, 10000, 20000]:
        px, se = mc_call_price(S, K, T, r, sigma, paths=paths, seed=seed)
        rows.append({'test': 'mc_convergence', 'grid': paths, 'price': px, 'stderr': se, 'benchmark': bs, 'abs_error': abs(px-bs), 'ci_covers_benchmark': abs(px-bs) <= 1.96*se})
    return pd.DataFrame(rows)
