# Executive Summary

Generated: 2026-06-04

## Purpose

This offline framework validates pricing/rates/risk models using benchmark comparison, backtesting, numerical reliability checks, and model-risk governance artifacts.

## Final decision

{'release_decision': 'PASS', 'validation_health_score': 92.0, 'critical_findings': 0, 'high_findings': 0, 'false_pass_rate': 0.0, 'claim_boundary': 'offline synthetic/public-data-sample independent validation framework; non-production; not regulatory-capital compliant'}

## Key metrics

Historical VaR99=24,056.41; Historical ES99=28,054.33; stressed VaR multiplier=1.15; PLA proxy correlation=0.929; APL/HPL corr=0.929; LH-ES component sum=50,696.34; baseline false-pass rate=0.000; relative false-pass reduction=100.0%; release=PASS.

## Safe resume wording

Independent Python quant model validation framework with derivatives, rates, Monte Carlo, VaR/ES, backtesting, numerical reliability, validation memos, and synthetic/public-data claim boundaries.
