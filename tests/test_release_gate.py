import pandas as pd
from governance.release_gate import release_decision


def test_release_gate_blocks_critical():
    findings = pd.DataFrame({'severity':['CRITICAL']})
    dec = release_decision(90, findings, 0.0)
    assert dec['release_decision'] == 'BLOCK'


def test_release_gate_passes_clean():
    findings = pd.DataFrame({'severity':['LOW']})
    dec = release_decision(90, findings, 0.0)
    assert dec['release_decision'] == 'PASS'
