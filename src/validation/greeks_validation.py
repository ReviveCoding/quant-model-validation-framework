import numpy as np
import pandas as pd
from models.black_scholes import bs_call_greeks
from benchmarks.finite_difference_checks import finite_diff_delta, finite_diff_gamma


def validate_greeks(option_df, sample_size=60):
    rows = []
    sample = option_df.head(sample_size)
    for _, row in sample.iterrows():
        analytic = bs_call_greeks(row['S'], row['K'], row['T'], row['r'], row['sigma'])
        fd_delta = finite_diff_delta(row['S'], row['K'], row['T'], row['r'], row['sigma'])
        fd_gamma = finite_diff_gamma(row['S'], row['K'], row['T'], row['r'], row['sigma'])
        rows.append({
            'option_id': row['option_id'],
            'delta_analytic': analytic['delta'],
            'delta_fd': fd_delta,
            'delta_abs_error': abs(analytic['delta'] - fd_delta),
            'gamma_analytic': analytic['gamma'],
            'gamma_fd': fd_gamma,
            'gamma_abs_error': abs(analytic['gamma'] - fd_gamma),
        })
    out = pd.DataFrame(rows)
    out['status'] = np.where((out.delta_abs_error < 1e-3) & (out.gamma_abs_error < 1e-3), 'PASS', 'REVIEW')
    return out
