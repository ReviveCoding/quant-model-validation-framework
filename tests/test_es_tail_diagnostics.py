from data.generate_synthetic_market import generate_synthetic_market
from risk.portfolio_var import historical_var_es, monte_carlo_var_es
from risk.es_tail_diagnostics import es_tail_diagnostics
import pandas as pd


def test_es_tail_diagnostics_runs():
    market = generate_synthetic_market(n_days=800)
    hvar, hes = historical_var_es(market['portfolio_pnl'])
    nvar, nes = monte_carlo_var_es(market['portfolio_pnl'])
    df = pd.DataFrame([
        {'method': 'historical', 'VaR_99': hvar, 'ES_99': hes},
        {'method': 'normal_monte_carlo', 'VaR_99': nvar, 'ES_99': nes},
    ])
    out = es_tail_diagnostics(market['portfolio_pnl'], df)
    assert len(out) == 2
    assert (out['tail_observations'] > 0).all()
    assert set(out['status']).issubset({'PASS', 'REVIEW'})
