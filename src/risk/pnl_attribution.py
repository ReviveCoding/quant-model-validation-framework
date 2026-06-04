import numpy as np
import pandas as pd


def pnl_attribution_proxy(market_df):
    """Proxy actual-vs-explained P&L attribution using available synthetic risk factors.

    Produces desk-style validation diagnostics: correlation, RMSE, unexplained share,
    and slope/intercept sanity checks. This is not an official FRTB PLA test.
    """
    df = market_df.copy()
    actual = df['portfolio_pnl'].astype(float).to_numpy()
    components = pd.DataFrame({
        'equity_component': 1_000_000 * 0.65 * df['equity_return'].astype(float),
        'rates_component': 1_000_000 * (-2.5) * df['rate_change'].astype(float),
        'spread_component': 1_000_000 * (-1.8) * df['spread_change'].astype(float),
        # intentionally omit idiosyncratic noise; unexplained component measures residual risk
    })
    explained = components.sum(axis=1).to_numpy()
    residual = actual - explained
    corr = float(np.corrcoef(actual, explained)[0, 1]) if len(actual) > 2 else np.nan
    rmse = float(np.sqrt(np.mean(residual ** 2)))
    actual_std = float(np.std(actual, ddof=1))
    unexplained_share = float(rmse / actual_std) if actual_std else np.nan
    # Simple regression slope of actual on explained
    slope = float(np.cov(explained, actual, ddof=1)[0, 1] / np.var(explained, ddof=1)) if np.var(explained, ddof=1) else np.nan
    detail = pd.concat([df[['date']].reset_index(drop=True), components], axis=1)
    detail['actual_pnl'] = actual
    detail['explained_pnl_proxy'] = explained
    detail['unexplained_pnl'] = residual
    summary = pd.DataFrame([{
        'pla_proxy_correlation': corr,
        'pla_proxy_rmse': rmse,
        'actual_pnl_std': actual_std,
        'unexplained_share': unexplained_share,
        'actual_on_explained_slope': slope,
        'status': 'PASS' if corr >= 0.90 and unexplained_share <= 0.40 else 'REVIEW',
        'residual_risk_budget': 0.40,
        'claim_boundary': 'P&L attribution proxy only; not an official FRTB PLA test'
    }])
    component_summary = components.assign(total_explained=explained).agg(['mean', 'std', 'min', 'max']).T.reset_index().rename(columns={'index': 'component'})
    return detail, summary, component_summary
