import pandas as pd
from models.black_scholes import bs_call_price
from validation.no_arbitrage_checks import call_no_arbitrage_checks


def test_no_arbitrage_passes():
    df = pd.DataFrame({'S':[100], 'K':[100], 'T':[1], 'r':[0.03], 'sigma':[0.25]})
    df['bs_price'] = bs_call_price(df['S'], df['K'], df['T'], df['r'], df['sigma'])
    out = call_no_arbitrage_checks(df)
    assert out.iloc[0]['status'] == 'PASS'
