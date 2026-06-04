import numpy as np
import pandas as pd


def risk_factor_modellability_proxy(public_panel):
    """FRTB-inspired data sufficiency / modellability proxy for public sample factors.

    It uses observation count, non-missing observations, stale share, and max date gaps.
    This is deliberately framed as a proxy diagnostic, not a formal modellability decision.
    """
    panel = public_panel.copy().sort_values('date')
    rows = []
    for col in [c for c in panel.columns if c != 'date' and not c.endswith('_shock')]:
        s = panel[['date', col]].dropna().copy()
        if s.empty:
            rows.append({'risk_factor': col, 'observations': 0, 'non_missing_observations': 0, 'max_business_day_gap': np.nan, 'stale_share': np.nan, 'modellability_proxy': 'NON_MODELLABLE_PROXY', 'status': 'REVIEW'})
            continue
        dates = pd.to_datetime(s['date'])
        gaps = dates.diff().dt.days.dropna()
        stale_share = float(s[col].astype(float).diff().abs().fillna(1).eq(0).mean())
        non_missing = int(s[col].notna().sum())
        max_gap = int(gaps.max()) if len(gaps) else 0
        modellable = non_missing >= 250 and stale_share <= 0.10 and max_gap <= 7
        rows.append({
            'risk_factor': col,
            'observations': int(len(panel)),
            'non_missing_observations': non_missing,
            'max_calendar_day_gap': max_gap,
            'stale_share': stale_share,
            'modellability_proxy': 'MODELLABLE_PROXY' if modellable else 'NON_MODELLABLE_PROXY',
            'status': 'PASS' if modellable else 'REVIEW',
            'claim_boundary': 'FRTB-inspired data-sufficiency proxy; not a formal modellability assessment'
        })
    return pd.DataFrame(rows)
