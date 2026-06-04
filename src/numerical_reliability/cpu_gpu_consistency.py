import pandas as pd


def cpu_gpu_consistency_stub(cpu_value, gpu_value=None, tolerance=0.005):
    # Portfolio-safe scaffold: if GPU value is unavailable, mark as NOT_RUN rather than claiming GPU execution.
    if gpu_value is None:
        return pd.DataFrame([{'check': 'cpu_gpu_consistency', 'cpu_value': cpu_value, 'gpu_value': None, 'relative_error': None, 'status': 'NOT_RUN'}])
    rel = abs(cpu_value - gpu_value) / max(abs(cpu_value), 1e-12)
    return pd.DataFrame([{'check': 'cpu_gpu_consistency', 'cpu_value': cpu_value, 'gpu_value': gpu_value, 'relative_error': rel, 'status': 'PASS' if rel <= tolerance else 'REVIEW'}])
