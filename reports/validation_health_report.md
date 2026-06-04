# Validation Health Report

Generated: 2026-06-04

## Health score

|   validation_health_score |   finding_penalty | health_decision   |
|--------------------------:|------------------:|:------------------|
|                        92 |                 8 | PASS              |

## False-pass rate

0.0

## Baseline vs final validation summary

| metric                        | value   | interpretation                                                                                        |
|:------------------------------|:--------|:------------------------------------------------------------------------------------------------------|
| baseline_false_pass_rate      | 0.0625  | Naive tolerance-only gate passing cases with one-sided underestimation risk.                          |
| final_false_pass_rate         | 0.0     | False-pass rate after residual challenger, asymmetric envelope, and release gate.                     |
| relative_false_pass_reduction | 1.0     | Relative reduction from baseline to final validation framework.                                       |
| baseline_risky_cases          | 7       | Cases caught only after applying one-sided risk-underestimation logic.                                |
| final_block_cases             | 1       | Final asymmetric-envelope BLOCK cases after residual correction.                                      |
| high_or_critical_findings     | 0       | Findings requiring review or blocking release.                                                        |
| final_release_decision        | PASS    | PASS/REVIEW/BLOCK decision from validation health score, finding severity, and final false-pass rate. |

## ES tail diagnostics

| method                |   alpha |   var_99 |   es_99 |   es_var_ratio |   tail_observations |   exceedance_rate |   realized_tail_mean_loss |   es_minus_realized_tail_mean | status   | claim_boundary                                                               |
|:----------------------|--------:|---------:|--------:|---------------:|--------------------:|------------------:|--------------------------:|------------------------------:|:---------|:-----------------------------------------------------------------------------|
| historical            |    0.99 |  24056.4 | 28054.3 |        1.16619 |                   8 |           0.01    |                   28054.3 |                         0     | PASS     | ES tail diagnostic for model validation; not a formal regulatory ES backtest |
| normal_monte_carlo    |    0.99 |  25093.1 | 29001   |        1.15574 |                   7 |           0.00875 |                   28502.3 |                       498.725 | PASS     | ES tail diagnostic for model validation; not a formal regulatory ES backtest |
| student_t_monte_carlo |    0.99 |  28237.3 | 39991   |        1.41625 |                   3 |           0.00375 |                   31076.3 |                      8914.68  | PASS     | ES tail diagnostic for model validation; not a formal regulatory ES backtest |

## APL/HPL proxy comparison

|   apl_recent_250_exceptions |   hpl_recent_250_exceptions |   apl_hpl_exception_gap |   apl_hpl_correlation |   residual_std_share | status   | claim_boundary                                                            |
|----------------------------:|----------------------------:|------------------------:|----------------------:|---------------------:|:---------|:--------------------------------------------------------------------------|
|                           3 |                           4 |                       1 |               0.92933 |             0.369745 | PASS     | APL/HPL backtesting proxy only; not an official FRTB P&L attribution test |

## Asymmetric envelope status counts

| asymmetric_status   |   count |
|:--------------------|--------:|
| PASS                |      72 |
| REVIEW              |       7 |
| BLOCK               |       1 |
