import numpy as np
from risk.portfolio_var import rolling_backtest_var
from validation.kupiec_test import kupiec_pof_test
from validation.christoffersen_test import christoffersen_independence_test


def test_backtesting_outputs():
    rng = np.random.default_rng(2)
    pnl = rng.normal(0, 1000, 400)
    bt = rolling_backtest_var(pnl, window=250, alpha=0.99)
    assert len(bt) == 150
    assert 'exception' in bt.columns
    kup = kupiec_pof_test(bt['exception'].sum(), len(bt), 0.99)
    chr_res = christoffersen_independence_test(bt['exception'].astype(int).to_numpy())
    assert kup['test'] == 'kupiec_pof'
    assert chr_res['test'] == 'christoffersen_independence'
