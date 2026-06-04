import numpy as np
import pandas as pd
from scipy.stats import t


def var_es(losses, alpha=0.99):
    losses = np.asarray(losses, dtype=float)
    var = np.quantile(losses, alpha)
    tail = losses[losses >= var]
    es = tail.mean() if len(tail) else var
    return float(var), float(es)


def historical_var_es(pnl, alpha=0.99):
    losses = -np.asarray(pnl, dtype=float)
    return var_es(losses, alpha)


def monte_carlo_var_es(pnl, alpha=0.99, sims=10000, seed=101, heavy_tail=False):
    rng = np.random.default_rng(seed)
    mu = np.mean(pnl)
    sigma = np.std(pnl, ddof=1)
    if heavy_tail:
        sim_pnl = mu + sigma * t(df=5).rvs(size=sims, random_state=rng) / np.sqrt(5/(5-2))
    else:
        sim_pnl = rng.normal(mu, sigma, sims)
    return var_es(-sim_pnl, alpha)


def rolling_backtest_var(pnl_series, window=250, alpha=0.99):
    pnl = np.asarray(pnl_series, dtype=float)
    rows = []
    for i in range(window, len(pnl)):
        hist = pnl[i-window:i]
        var, es = historical_var_es(hist, alpha)
        loss = -pnl[i]
        rows.append({'index': i, 'actual_pnl': pnl[i], 'actual_loss': loss, 'var_99': var, 'es_99': es, 'exception': loss > var, 'exception_severity': max(loss - var, 0)})
    return pd.DataFrame(rows)
