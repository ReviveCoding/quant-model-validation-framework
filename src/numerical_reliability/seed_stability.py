import numpy as np
import pandas as pd
from models.monte_carlo_option import mc_call_price


def seed_stability_case(S=100, K=100, T=1.0, r=0.03, sigma=0.25, paths=10000):
    rows = []
    for seed in [7, 11, 19, 23, 31]:
        price, stderr = mc_call_price(S, K, T, r, sigma, paths=paths, seed=seed)
        rows.append({'seed': seed, 'price': price, 'stderr': stderr})
    df = pd.DataFrame(rows)
    df['price_std_across_seeds'] = df['price'].std(ddof=1)
    df['relative_std'] = df['price'].std(ddof=1) / max(abs(df['price'].mean()), 1e-8)
    return df
