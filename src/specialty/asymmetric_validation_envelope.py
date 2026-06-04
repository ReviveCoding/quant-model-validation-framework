import numpy as np
import pandas as pd


def asymmetric_envelope(df, error_col='mc_error', underestimation_col='risk_underestimation'):
    out = df.copy()
    # Underestimation gets stronger penalty because false comfort is more dangerous in risk validation.
    out['asymmetric_penalty'] = np.where(out[underestimation_col], 2.5 * np.abs(out[error_col]), np.abs(out[error_col]))
    out['asymmetric_status'] = 'PASS'
    out.loc[out['asymmetric_penalty'] > 0.08, 'asymmetric_status'] = 'REVIEW'
    out.loc[out['asymmetric_penalty'] > 0.20, 'asymmetric_status'] = 'BLOCK'
    return out
