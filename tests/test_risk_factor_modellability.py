from pathlib import Path
from data.generate_synthetic_market import create_public_sample_files
from data.public_market_data import validate_public_market_data
from validation.risk_factor_modellability import risk_factor_modellability_proxy


def test_modellability_proxy_public_sample(tmp_path: Path):
    create_public_sample_files(tmp_path)
    _, _, panel, _ = validate_public_market_data(tmp_path)
    out = risk_factor_modellability_proxy(panel)
    assert len(out) >= 4
    assert set(out['modellability_proxy']).issubset({'MODELLABLE_PROXY','NON_MODELLABLE_PROXY'})
    assert (out['non_missing_observations'] >= 250).all()
