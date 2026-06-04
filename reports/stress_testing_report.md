# Stress Testing Report

Generated: 2026-06-04

## Stress loss by scenario

| scenario                 |   base_value |   stressed_value |   stress_loss |
|:-------------------------|-------------:|-----------------:|--------------:|
| equity_down_10_vol_up    |      64018.3 |          54101.5 |      9916.81  |
| equity_down_25_vol_spike |      64018.3 |          43214.4 |     20804     |
| rate_up_100bp            |      64018.3 |          64194.4 |      -176.055 |
| liquidity_spread_stress  |      64018.3 |          60483   |      3535.36  |

## Stress scenario coverage and monotonicity checks

| check                               | value   | status   |
|:------------------------------------|:--------|:---------|
| has_equity_down_scenario            | True    | PASS     |
| has_volatility_up_scenario          | True    | PASS     |
| has_rate_up_scenario                | True    | PASS     |
| equity_vol_ladder_loss_monotonicity | True    | PASS     |
