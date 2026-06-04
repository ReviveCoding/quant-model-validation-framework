import numpy as np
import pandas as pd
from risk.portfolio_var import historical_var_es


def stressed_var_window(pnl_series, window=250, alpha=0.99, stress_window=60):
    """Select a historical window with the largest rolling VaR and compute stressed VaR/ES.

    This is an educational/stress-diagnostic proxy, not a regulatory stressed-VaR model.
    Selecting by rolling VaR, rather than volatility alone, better aligns the proxy with tail-loss
    validation and avoids picking a volatile but non-tail-severe window.
    """
    pnl = pd.Series(np.asarray(pnl_series, dtype=float)).reset_index(drop=True)
    if len(pnl) < max(window, stress_window) + 5:
        raise ValueError("pnl_series must be longer than the VaR and stress windows")

    full_var, full_es = historical_var_es(pnl, alpha=alpha)
    best = None
    for end_idx in range(stress_window, len(pnl) + 1):
        start_idx = end_idx - stress_window
        sample = pnl.iloc[start_idx:end_idx]
        win_var, win_es = historical_var_es(sample, alpha=alpha)
        if best is None or win_var > best['stressed_var']:
            best = {
                'selected_start_index': start_idx,
                'selected_end_index': end_idx - 1,
                'selected_window_observations': int(len(sample)),
                'selected_window_pnl_volatility': float(sample.std(ddof=1)),
                'stressed_var': float(win_var),
                'stressed_es': float(win_es),
            }

    full_vol = float(pnl.std(ddof=1))
    stressed_var = best['stressed_var']
    stressed_es = best['stressed_es']
    multiplier = float(stressed_var / full_var) if full_var else np.nan
    status = 'REVIEW' if multiplier > 1.25 else 'PASS'
    return pd.DataFrame([{
        'method': 'max_rolling_var_stressed_window_proxy',
        'alpha': alpha,
        'stress_window_days': stress_window,
        'selected_start_index': best['selected_start_index'],
        'selected_end_index': best['selected_end_index'],
        'selected_window_observations': best['selected_window_observations'],
        'selected_window_pnl_volatility': best['selected_window_pnl_volatility'],
        'full_sample_pnl_volatility': full_vol,
        'full_sample_var': float(full_var),
        'full_sample_es': float(full_es),
        'stressed_var': stressed_var,
        'stressed_es': stressed_es,
        'stressed_var_multiplier': multiplier,
        'stressed_es_multiplier': float(stressed_es / full_es) if full_es else np.nan,
        'selection_rule': 'maximum rolling historical VaR over candidate stress windows',
        'status': status,
        'claim_boundary': 'stressed-window proxy for validation; not a regulatory stressed-VaR model'
    }])
