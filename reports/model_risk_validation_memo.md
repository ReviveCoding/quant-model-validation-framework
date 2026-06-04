# Model Risk Validation Memo

Generated: 2026-06-04

## Executive finding

Release decision: PASS with validation health score 92.0.

## Model-risk findings

| finding_id   | area                     | severity   | description                                                                   | recommendation                                                                 |
|:-------------|:-------------------------|:-----------|:------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| F009         | subportfolio_backtesting | MEDIUM     | 1 subportfolio backtesting proxy segment(s) are in yellow traffic-light zone. | Monitor subportfolio exceptions and document risk-factor-specific limitations. |

## Claim boundary

offline synthetic/public-data-sample independent validation framework; non-production; not regulatory-capital compliant

## Compensating controls

Benchmark comparison, numerical tolerance gates, asymmetric validation envelope, stressed-window VaR proxy, P&L attribution proxy, and release gate are required before use.
