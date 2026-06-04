# Project Card

## Project
Quant Model Validation & Numerical Risk Simulation Framework

## Purpose
Create a runnable, non-production independent model-validation framework showing quant fundamentals, validation discipline, numerical reliability, and governance-ready reporting for market-risk/model-validation roles.

## Data
- Default: synthetic option/rates/market-risk portfolios.
- Optional sample: local public-data-shaped Treasury rate and OAS sample files.
- No proprietary bank, client, customer, or trading-desk data.

## Methods
Black-Scholes, binomial tree, Monte Carlo pricing, Heston simulation, Vasicek/CIR rate models, VaR, Expected Shortfall, full revaluation, delta-gamma approximation, stress testing, Kupiec and Christoffersen backtesting.

## Reliability layer
Validation Health Score, residual error-correction challenger, asymmetric validation envelope, numerical tolerance gates, convergence diagnostics, model-risk findings, release gate.

## Governance
Validation memo, model card, known limitations, compensating controls, executive summary, model inventory, model-risk findings, release decision.

## Claim boundary
Offline portfolio project. Not production. Not regulatory-capital compliant. Uses synthetic portfolios and public-data samples only.


## Enhanced v2 additions

- Added public-data sample validation for H.15-style Treasury rates and FRED ICE BofA OAS-style spread factors.
- Added subportfolio VaR backtesting proxies for derivatives, rates, spread-risk, and aggregate P&L.
- Added regulatory-style mapping memo for VaR/ES/backtesting/stress/assumption testing artifacts.
- Added baseline-vs-final validation summary with one-sided false-pass reduction metrics.
- Added `reports/resume_metrics_report.md` to separate resume-safe evidence from non-production claim boundaries.


## Enhanced v3 additions

- Added stressed-window VaR proxy using maximum rolling historical VaR selection rather than volatility-only window selection.
- Added P&L attribution proxy with actual-vs-explained P&L correlation, unexplained-share diagnostics, component summaries, and residual-risk budget.
- Added FRTB-inspired risk-factor modellability/data-sufficiency proxy for public-data sample factors.
- Corrected traffic-light reporting to use the most recent 250 observations for regulatory-style display while preserving full-sample outcomes analysis.
- Added GitHub Actions CI workflow and local/GitHub runnable structure audit.
- Added subportfolio-specific model-risk finding when any subportfolio proxy is in yellow/red traffic-light status.


## Final enhancement loop additions

- Added APL/HPL backtesting proxy to separate actual synthetic P&L from hypothetical/explained P&L.
- Added ES tail diagnostics to compare reported ES values against realized average losses beyond VaR thresholds.
- Added FRTB-inspired liquidity-horizon ES proxy for derivatives, rates, spread-risk, and aggregate P&L proxies.
- Added stress scenario coverage and monotonicity checks for scenario-design QA.
- Added artifact manifest, run manifest, Dockerfile, and expanded GitHub runnable audit.

Claim boundary: all additions are educational/model-validation proxies using synthetic/public-data samples; they are not official FRTB, regulatory-capital, or production trading-desk calculations.
