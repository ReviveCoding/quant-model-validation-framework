import pandas as pd


def apply_tolerance_gate(df, error_col='abs_error', warn=0.05, block=0.15):
    out = df.copy()
    out['gate'] = 'PASS'
    out.loc[out[error_col] > warn, 'gate'] = 'REVIEW'
    out.loc[out[error_col] > block, 'gate'] = 'BLOCK'
    return out
