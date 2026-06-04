from pathlib import Path
from data.generate_synthetic_market import create_public_sample_files
from data.public_market_data import validate_public_market_data


def test_public_market_data_validation(tmp_path: Path):
    create_public_sample_files(tmp_path)
    checks, summary, panel, corr = validate_public_market_data(tmp_path)
    assert not checks.empty
    assert not summary.empty
    assert 'DGS10_shock' in panel.columns
    assert 'risk_factor' in corr.columns
