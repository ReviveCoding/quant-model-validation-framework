import numpy as np
from risk.portfolio_var import historical_var_es, monte_carlo_var_es


def test_var_es_ordering():
    rng = np.random.default_rng(0)
    pnl = rng.normal(0, 1000, 1000)
    var, es = historical_var_es(pnl, 0.99)
    assert es >= var > 0


def test_mc_var_positive():
    rng = np.random.default_rng(1)
    pnl = rng.normal(0, 1000, 500)
    var, es = monte_carlo_var_es(pnl, 0.99)
    assert es >= var > 0
