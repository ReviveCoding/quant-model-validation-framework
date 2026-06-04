import pandas as pd
from risk.portfolio_var import historical_var_es, monte_carlo_var_es


def assumption_sensitivity(pnl):
    rows = []
    for alpha in [0.95, 0.99]:
        hvar, hes = historical_var_es(pnl, alpha)
        nvar, nes = monte_carlo_var_es(pnl, alpha, heavy_tail=False)
        tvar, tes = monte_carlo_var_es(pnl, alpha, heavy_tail=True)
        rows.extend([
            {'assumption': f'historical_alpha_{alpha}', 'VaR': hvar, 'ES': hes},
            {'assumption': f'normal_mc_alpha_{alpha}', 'VaR': nvar, 'ES': nes},
            {'assumption': f'student_t_mc_alpha_{alpha}', 'VaR': tvar, 'ES': tes},
        ])
    return pd.DataFrame(rows)
