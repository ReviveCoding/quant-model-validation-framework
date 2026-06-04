from data.generate_synthetic_market import generate_option_portfolio
from risk.stress_loss import option_portfolio_stress_loss
from validation.stress_scenario_coverage import stress_scenario_coverage


def test_stress_scenario_coverage_passes_ladder():
    portfolio = generate_option_portfolio()
    scenarios = [
        {'name': 'equity_down_10_vol_up', 'equity_shock': -0.10, 'volatility_shock': 0.10, 'rate_shock': 0.0025},
        {'name': 'equity_down_25_vol_spike', 'equity_shock': -0.25, 'volatility_shock': 0.25, 'rate_shock': 0.0050},
        {'name': 'rate_up_100bp', 'equity_shock': -0.03, 'volatility_shock': 0.05, 'rate_shock': 0.0100},
    ]
    stress = option_portfolio_stress_loss(portfolio, scenarios)
    out = stress_scenario_coverage(stress, scenarios)
    assert len(out) >= 4
    assert set(out['status']).issubset({'PASS', 'REVIEW'})
