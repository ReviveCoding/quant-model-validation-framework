import pandas as pd


def build_baseline_vs_final_summary(benchmark_gated: pd.DataFrame, asym: pd.DataFrame, findings: pd.DataFrame, decision: dict) -> pd.DataFrame:
    """Compare a naive tolerance-only baseline with the final validation stack.

    Baseline false-pass is intentionally computed from the uncorrected MC-vs-benchmark
    relative error and a one-sided risk-underestimation penalty. Final false-pass is
    computed after the residual challenger and asymmetric envelope. This makes the
    improvement interpretable rather than hiding baseline risk after correction.
    """
    baseline_pass = benchmark_gated['gate'].eq('PASS')
    baseline_under = benchmark_gated.get('risk_underestimation', pd.Series(False, index=benchmark_gated.index)).astype(bool)
    baseline_rel = benchmark_gated['rel_abs_error'].abs()
    baseline_risky = baseline_under & ((2.5 * baseline_rel) > 0.08)

    final_risky = asym['asymmetric_status'].eq('BLOCK')
    final_pass = asym['asymmetric_status'].eq('PASS')

    baseline_false_pass = float((baseline_pass & baseline_risky).mean())
    final_false_pass = float((final_pass & final_risky).mean())
    reduction = 0.0 if baseline_false_pass == 0 else (baseline_false_pass - final_false_pass) / baseline_false_pass
    return pd.DataFrame([
        {'metric': 'baseline_false_pass_rate', 'value': baseline_false_pass, 'interpretation': 'Naive tolerance-only gate passing cases with one-sided underestimation risk.'},
        {'metric': 'final_false_pass_rate', 'value': final_false_pass, 'interpretation': 'False-pass rate after residual challenger, asymmetric envelope, and release gate.'},
        {'metric': 'relative_false_pass_reduction', 'value': float(reduction), 'interpretation': 'Relative reduction from baseline to final validation framework.'},
        {'metric': 'baseline_risky_cases', 'value': int(baseline_risky.sum()), 'interpretation': 'Cases caught only after applying one-sided risk-underestimation logic.'},
        {'metric': 'final_block_cases', 'value': int(final_risky.sum()), 'interpretation': 'Final asymmetric-envelope BLOCK cases after residual correction.'},
        {'metric': 'high_or_critical_findings', 'value': int(findings['severity'].isin(['HIGH', 'CRITICAL']).sum()), 'interpretation': 'Findings requiring review or blocking release.'},
        {'metric': 'final_release_decision', 'value': decision['release_decision'], 'interpretation': 'PASS/REVIEW/BLOCK decision from validation health score, finding severity, and final false-pass rate.'},
    ])
