import pandas as pd
from specialty.asymmetric_validation_envelope import asymmetric_envelope
from specialty.validation_health_score import build_validation_health_score


def test_asymmetric_envelope_penalizes_underestimation():
    df = pd.DataFrame({'corrected_error':[0.1,0.1], 'risk_underestimation':[True, False]})
    out = asymmetric_envelope(df, 'corrected_error', 'risk_underestimation')
    assert out.loc[0,'asymmetric_penalty'] > out.loc[1,'asymmetric_penalty']


def test_health_score():
    findings = pd.DataFrame({'severity':['LOW','HIGH']})
    out = build_validation_health_score(findings)
    assert 0 <= out.iloc[0]['validation_health_score'] <= 100
