import pandas as pd
from models.black_scholes import bs_call_price


def option_portfolio_stress_loss(portfolio, scenarios):
    rows = []
    base_values = bs_call_price(portfolio['S'], portfolio['K'], portfolio['T'], portfolio['r'], portfolio['sigma']) * portfolio['position']
    base_total = float(base_values.sum())
    for sc in scenarios:
        stressed_s = portfolio['S'] * (1 + sc['equity_shock'])
        stressed_sigma = (portfolio['sigma'] + sc['volatility_shock']).clip(lower=0.01)
        stressed_r = portfolio['r'] + sc['rate_shock']
        stressed_values = bs_call_price(stressed_s, portfolio['K'], portfolio['T'], stressed_r, stressed_sigma) * portfolio['position']
        stressed_total = float(stressed_values.sum())
        rows.append({'scenario': sc['name'], 'base_value': base_total, 'stressed_value': stressed_total, 'stress_loss': base_total - stressed_total})
    return pd.DataFrame(rows)
