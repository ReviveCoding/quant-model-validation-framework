import pandas as pd
from data.generate_synthetic_market import generate_synthetic_market
from risk.stressed_var import stressed_var_window


def test_stressed_var_window_outputs_multiplier():
    market = generate_synthetic_market(n_days=420)
    out = stressed_var_window(market['portfolio_pnl'], stress_window=40)
    assert {'stressed_var', 'stressed_es', 'stressed_var_multiplier', 'status'}.issubset(out.columns)
    assert out['selected_window_observations'].iloc[0] == 40
    assert out['stressed_var'].iloc[0] > 0
