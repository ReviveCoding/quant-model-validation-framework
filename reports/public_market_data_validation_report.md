# Public Market Data Validation Report

Generated: 2026-06-04

## Purpose

Validates public-data-shaped Federal Reserve H.15 Treasury-rate and FRED ICE BofA OAS sample files used for rates/spread sanity checks.

## Series-level checks

| series       |   observations |   missing_count |   missing_share |   stale_count |   outlier_shock_count |   min_value |   max_value |   mean_daily_abs_shock | status   |
|:-------------|---------------:|----------------:|----------------:|--------------:|----------------------:|------------:|------------:|-----------------------:|:---------|
| DGS2         |            260 |               0 |               0 |             0 |                     0 |   0.0273429 |   0.0362241 |            0.000267726 | PASS     |
| DGS10        |            260 |               0 |               0 |             0 |                     0 |   0.0364409 |   0.0433039 |            0.000249871 | PASS     |
| BAMLC0A0CM   |            260 |               0 |               0 |             0 |                     0 |   0.0103929 |   0.0157442 |            0.000202585 | PASS     |
| BAMLH0A0HYM2 |            260 |               0 |               0 |             0 |                     0 |   0.0358889 |   0.0474545 |            0.000553417 | PASS     |

## Risk-factor shock summary

| risk_factor        |   mean_shock |   volatility |    p01_shock |   p99_shock |
|:-------------------|-------------:|-------------:|-------------:|------------:|
| DGS2_shock         | -2.48467e-05 |  0.000349078 | -0.000789578 | 0.000803455 |
| DGS10_shock        |  9.43417e-06 |  0.000310706 | -0.000707111 | 0.000709351 |
| BAMLC0A0CM_shock   |  1.07426e-06 |  0.000255309 | -0.000554982 | 0.000548927 |
| BAMLH0A0HYM2_shock |  1.74646e-05 |  0.000674692 | -0.00127596  | 0.00169747  |

## Correlation matrix

| risk_factor        |   DGS2_shock |   DGS10_shock |   BAMLC0A0CM_shock |   BAMLH0A0HYM2_shock |
|:-------------------|-------------:|--------------:|-------------------:|---------------------:|
| DGS2_shock         |    1         |     0.0498451 |         -0.0714446 |            0.0742171 |
| DGS10_shock        |    0.0498451 |     1         |         -0.110877  |            0.0672441 |
| BAMLC0A0CM_shock   |   -0.0714446 |    -0.110877  |          1         |           -0.143158  |
| BAMLH0A0HYM2_shock |    0.0742171 |     0.0672441 |         -0.143158  |            1         |

## FRTB-inspired data-sufficiency proxy

| risk_factor   |   observations |   non_missing_observations |   max_calendar_day_gap |   stale_share | modellability_proxy   | status   | claim_boundary                                                              |
|:--------------|---------------:|---------------------------:|-----------------------:|--------------:|:----------------------|:---------|:----------------------------------------------------------------------------|
| DGS2          |            260 |                        260 |                      3 |             0 | MODELLABLE_PROXY      | PASS     | FRTB-inspired data-sufficiency proxy; not a formal modellability assessment |
| DGS10         |            260 |                        260 |                      3 |             0 | MODELLABLE_PROXY      | PASS     | FRTB-inspired data-sufficiency proxy; not a formal modellability assessment |
| BAMLC0A0CM    |            260 |                        260 |                      3 |             0 | MODELLABLE_PROXY      | PASS     | FRTB-inspired data-sufficiency proxy; not a formal modellability assessment |
| BAMLH0A0HYM2  |            260 |                        260 |                      3 |             0 | MODELLABLE_PROXY      | PASS     | FRTB-inspired data-sufficiency proxy; not a formal modellability assessment |

## Claim boundary

Sample/fallback public-data mode only; no live proprietary market data or trading-book positions.
