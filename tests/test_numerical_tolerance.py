import pandas as pd
from numerical_reliability.tolerance_gates import apply_tolerance_gate
from numerical_reliability.cpu_gpu_consistency import cpu_gpu_consistency_stub


def test_tolerance_gate_statuses():
    df = pd.DataFrame({'abs_error':[0.01, 0.07, 0.20]})
    out = apply_tolerance_gate(df, 'abs_error', warn=0.05, block=0.15)
    assert list(out['gate']) == ['PASS', 'REVIEW', 'BLOCK']


def test_cpu_gpu_not_run_safe():
    out = cpu_gpu_consistency_stub(1.0)
    assert out.iloc[0]['status'] == 'NOT_RUN'
