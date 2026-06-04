# Regulatory Mapping Memo

Generated: 2026-06-04

## Purpose

Maps market-risk/model-validation concepts to implemented project artifacts without claiming regulatory compliance.

## Mapping table

| requirement_or_concept                                   | project_artifact                                                                 | implementation                                                                                          | claim_boundary                                                   |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------|
| 250-business-day VaR backtesting                         | outputs/backtesting_exceptions.csv; outputs/subportfolio_backtesting_summary.csv | Rolling one-day VaR backtesting with exception counts and severity by aggregate and subportfolio proxy. | Regulatory-style diagnostic only; not a bank capital model.      |
| 99% one-tail VaR                                         | outputs/var_es_results.csv                                                       | Historical, normal Monte Carlo, and Student-t Monte Carlo VaR99/ES99 estimates.                         | Synthetic portfolio and sample public-data mode.                 |
| Expected Shortfall / FRTB-inspired tail-risk diagnostics | outputs/var_es_results.csv; reports/assumption_impact_report.md                  | ES99 and heavy-tail sensitivity to show tail-risk behavior beyond VaR.                                  | FRTB-inspired; not FRTB-compliant.                               |
| Alternative modeling assumptions                         | outputs/assumption_sensitivity_matrix.csv                                        | Historical vs Monte Carlo, normal vs Student-t, and volatility scaling comparisons.                     | Model-development benchmark evidence, not production validation. |
| Model limitations and compensating controls              | reports/known_limitations.md; reports/compensating_controls.md                   | Explicit documentation of synthetic data, model-use limits, challenger checks, and release gates.       | Non-production portfolio project.                                |
