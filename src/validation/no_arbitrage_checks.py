import pandas as pd


def call_no_arbitrage_checks(df):
    # European call lower bound: max(S - K exp(-rT), 0), upper bound: S.
    lower = (df['S'] - df['K'] * (2.718281828459045 ** (-df['r'] * df['T']))).clip(lower=0)
    upper = df['S']
    violation = (df['bs_price'] < lower - 1e-8) | (df['bs_price'] > upper + 1e-8)
    return pd.DataFrame({
        'check': ['call_lower_upper_bound'],
        'violations': [int(violation.sum())],
        'status': ['PASS' if violation.sum() == 0 else 'BLOCK']
    })
