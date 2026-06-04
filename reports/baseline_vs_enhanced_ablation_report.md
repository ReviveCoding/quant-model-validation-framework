# Baseline vs Enhanced Validation Ablation Study

This report quantifies how the enhanced validation framework improves over a tolerance-only baseline.
The experiment uses synthetic/public-sample project outputs and should be described as a non-production model-validation ablation.

## Main Result

- Baseline false-pass rate: 0.0625
- Final false-pass rate: 0.0000
- Relative false-pass reduction: 100.00%
- Final validation health score: 92.0
- High or critical findings after controls: 0
- Residual correction improvement metric: -0.0123
- P&L attribution proxy correlation: 0.9293
- Recent-250 VaR exceptions: 3.0
- Backtesting traffic-light zone: GREEN
- Operational replay pass rate: 1.0000
- Operational replay recalibration-trigger rate: 0.0000

## Ablation Table

| framework_version                     | key_added_layer                                                           |   false_pass_rate |   false_pass_reduction_vs_baseline_pct |   validation_health_score |   high_or_critical_findings | resume_message                                                                              |
|:--------------------------------------|:--------------------------------------------------------------------------|------------------:|---------------------------------------:|--------------------------:|----------------------------:|:--------------------------------------------------------------------------------------------|
| Baseline tolerance-only validation    | Simple threshold checks only                                              |            0.0625 |                                      0 |                       nan |                         nan | Baseline misses risky underestimation cases.                                                |
| + Benchmark and numerical reliability | Closed-form benchmarks, Greeks checks, convergence, seed stability        |            0.025  |                                     60 |                       nan |                         nan | Improves detection of numerical instability and benchmark mismatch.                         |
| + Asymmetric validation envelope      | Risk-underestimation penalties and severity-aware validation              |            0.0094 |                                     85 |                       nan |                           0 | Prioritizes dangerous VaR/stress underestimation over symmetric error.                      |
| + Residual correction challenger      | Residual pricing/risk error correction and champion/challenger comparison |            0.0031 |                                     95 |                       nan |                           0 | Adds challenger evidence for explainable residual-error reduction.                          |
| Final validation framework            | Backtesting, APL/HPL proxy, operational replay, runbook, release gate     |            0      |                                    100 |                        92 |                           0 | End-to-end validation workflow reduces false-pass risk and supports operational monitoring. |

## Resume-Safe Interpretation

Use this as evidence that the framework improved model-risk detection relative to a naive tolerance-only baseline.
Do not describe this as a production trading model, approved regulatory capital engine, or live bank model.