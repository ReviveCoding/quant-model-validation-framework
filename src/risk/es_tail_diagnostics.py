import numpy as np
import pandas as pd


def es_tail_diagnostics(pnl_series, var_es_df: pd.DataFrame, alpha: float = 0.99) -> pd.DataFrame:
    """Compare model ES values against realized tail loss means under synthetic P&L.

    This diagnostic is not a regulatory ES backtest. It is a transparent outcomes-analysis
    check that asks whether the reported ES is at least as conservative as the realized
    average loss beyond each method's VaR threshold.
    """
    pnl = pd.Series(np.asarray(pnl_series, dtype=float))
    loss = -pnl
    rows = []
    for _, row in var_es_df.iterrows():
        var = float(row['VaR_99'])
        es = float(row['ES_99'])
        tail = loss[loss >= var]
        realized_tail_mean = float(tail.mean()) if len(tail) else 0.0
        exceedance_rate = float(len(tail) / max(len(loss), 1))
        es_gap = float(es - realized_tail_mean)
        rows.append({
            'method': row['method'],
            'alpha': alpha,
            'var_99': var,
            'es_99': es,
            'es_var_ratio': float(es / var) if var else np.nan,
            'tail_observations': int(len(tail)),
            'exceedance_rate': exceedance_rate,
            'realized_tail_mean_loss': realized_tail_mean,
            'es_minus_realized_tail_mean': es_gap,
            'status': 'PASS' if es_gap >= -0.05 * max(realized_tail_mean, 1.0) else 'REVIEW',
            'claim_boundary': 'ES tail diagnostic for model validation; not a formal regulatory ES backtest'
        })
    return pd.DataFrame(rows)
