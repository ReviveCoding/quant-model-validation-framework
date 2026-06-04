# Model Operations Runbook

## Purpose
Provide a lightweight operating procedure for running the non-production quant model validation framework.

## Standard Run
```bash
python scripts/run_pipeline.py
python -m pytest -q
python scripts/evaluate_performance.py
python scripts/run_operational_replay.py
```

## Review Triggers
- Release decision is REVIEW or BLOCK.
- Validation health score drops below 85.
- False-pass rate is above 0.
- High or critical model-risk findings appear.
- Recent 250-day traffic-light zone is YELLOW or RED.

## Escalation
Document the breach, inspect model-risk findings, compare champion/challenger outputs, rerun assumption sensitivity, and record compensating controls.

## Claim Boundary
This runbook supports a local, synthetic/public-sample, non-production validation project. It does not claim production trading, official regulatory capital, or bank-approved model use.