# VaR and ES Backtesting Report

Generated: 2026-06-04

## VaR/ES results

| method                |   VaR_99 |   ES_99 |
|:----------------------|---------:|--------:|
| historical            |  24056.4 | 28054.3 |
| normal_monte_carlo    |  25093.1 | 29001   |
| student_t_monte_carlo |  28237.3 | 39991   |

## Stressed-window VaR proxy

| method                                |   alpha |   stress_window_days |   selected_start_index |   selected_end_index |   selected_window_observations |   selected_window_pnl_volatility |   full_sample_pnl_volatility |   full_sample_var |   full_sample_es |   stressed_var |   stressed_es |   stressed_var_multiplier |   stressed_es_multiplier | selection_rule                                               | status   | claim_boundary                                                            |
|:--------------------------------------|--------:|---------------------:|-----------------------:|---------------------:|-------------------------------:|---------------------------------:|-----------------------------:|------------------:|-----------------:|---------------:|--------------:|--------------------------:|-------------------------:|:-------------------------------------------------------------|:---------|:--------------------------------------------------------------------------|
| max_rolling_var_stressed_window_proxy |    0.99 |                   60 |                    498 |                  557 |                             60 |                          9738.97 |                      10652.3 |           24056.4 |          28054.3 |        27738.3 |         29338 |                   1.15305 |                  1.04576 | maximum rolling historical VaR over candidate stress windows | PASS     | stressed-window proxy for validation; not a regulatory stressed-VaR model |

## ES tail diagnostics

| method                |   alpha |   var_99 |   es_99 |   es_var_ratio |   tail_observations |   exceedance_rate |   realized_tail_mean_loss |   es_minus_realized_tail_mean | status   | claim_boundary                                                               |
|:----------------------|--------:|---------:|--------:|---------------:|--------------------:|------------------:|--------------------------:|------------------------------:|:---------|:-----------------------------------------------------------------------------|
| historical            |    0.99 |  24056.4 | 28054.3 |        1.16619 |                   8 |           0.01    |                   28054.3 |                         0     | PASS     | ES tail diagnostic for model validation; not a formal regulatory ES backtest |
| normal_monte_carlo    |    0.99 |  25093.1 | 29001   |        1.15574 |                   7 |           0.00875 |                   28502.3 |                       498.725 | PASS     | ES tail diagnostic for model validation; not a formal regulatory ES backtest |
| student_t_monte_carlo |    0.99 |  28237.3 | 39991   |        1.41625 |                   3 |           0.00375 |                   31076.3 |                      8914.68  | PASS     | ES tail diagnostic for model validation; not a formal regulatory ES backtest |

## Liquidity-horizon ES proxy

| subportfolio   |   alpha |   liquidity_horizon_days |   base_10day_es_proxy |   scaled_liquidity_horizon_es_proxy |   scaling_multiplier | claim_boundary                                                                 |   component_scaled_es_sum_proxy | status   |
|:---------------|--------:|-------------------------:|----------------------:|------------------------------------:|---------------------:|:-------------------------------------------------------------------------------|--------------------------------:|:---------|
| derivatives    |   0.975 |                       10 |              11519.6  |                            11519.6  |              1       | FRTB-inspired liquidity-horizon ES proxy; not a regulatory capital calculation |                         50696.3 | PASS     |
| rates          |   0.975 |                       20 |               5392.23 |                             7625.76 |              1.41421 | FRTB-inspired liquidity-horizon ES proxy; not a regulatory capital calculation |                         50696.3 | PASS     |
| spread_proxy   |   0.975 |                       60 |              12880.7  |                            31551    |              2.44949 | FRTB-inspired liquidity-horizon ES proxy; not a regulatory capital calculation |                         50696.3 | PASS     |
| aggregate      |   0.975 |                       10 |              24511    |                            24511    |              1       | FRTB-inspired liquidity-horizon ES proxy; not a regulatory capital calculation |                         50696.3 | PASS     |

## Backtesting summary

|   n_obs |   exceptions |   exception_rate |   severity_sum |   recent_250_obs |   recent_250_exceptions |   recent_250_exception_rate |   recent_250_severity_sum | traffic_light_zone   | traffic_light_basis          |
|--------:|-------------:|-----------------:|---------------:|-----------------:|------------------------:|----------------------------:|--------------------------:|:---------------------|:-----------------------------|
|     550 |            8 |        0.0145455 |        31586.8 |              250 |                       3 |                       0.012 |                   13062.7 | GREEN                | most_recent_250_observations |

## Kupiec/Christoffersen

| test                        |   exceptions |   n_obs |   lr_stat |   p_value | status   |
|:----------------------------|-------------:|--------:|----------:|----------:|:---------|
| kupiec_pof                  |            8 |     550 |  1.00659  |  0.315721 | PASS     |
| christoffersen_independence |          nan |     nan |  0.236608 |  0.626667 | PASS     |

## Subportfolio backtesting summary

| subportfolio   |   n_obs |   exceptions |   exception_rate |   severity_sum |   recent_250_obs |   recent_250_exceptions |   recent_250_exception_rate |   recent_250_severity_sum | traffic_light_zone   | traffic_light_basis          |
|:---------------|--------:|-------------:|-----------------:|---------------:|-----------------:|------------------------:|----------------------------:|--------------------------:|:---------------------|:-----------------------------|
| derivatives    |     550 |           10 |        0.0181818 |       20065.4  |              250 |                       6 |                       0.024 |                   5587.81 | YELLOW               | most_recent_250_observations |
| rates          |     550 |            7 |        0.0127273 |        5400.06 |              250 |                       4 |                       0.016 |                   3538.51 | GREEN                | most_recent_250_observations |
| spread_proxy   |     550 |            8 |        0.0145455 |       14944.8  |              250 |                       4 |                       0.016 |                   5543.36 | GREEN                | most_recent_250_observations |
| aggregate      |     550 |            8 |        0.0145455 |       31586.8  |              250 |                       3 |                       0.012 |                  13062.7  | GREEN                | most_recent_250_observations |

## Subportfolio statistical tests

| test                        |   exceptions |   n_obs |   lr_stat |   p_value | status   | subportfolio   |
|:----------------------------|-------------:|--------:|----------:|----------:|:---------|:---------------|
| kupiec_pof                  |           10 |     550 |  2.99403  | 0.0835718 | PASS     | derivatives    |
| christoffersen_independence |          nan |     nan |  0.371079 | 0.542417  | PASS     | derivatives    |
| kupiec_pof                  |            7 |     550 |  0.380405 | 0.537387  | PASS     | rates          |
| christoffersen_independence |          nan |     nan |  0.180817 | 0.670672  | PASS     | rates          |
| kupiec_pof                  |            8 |     550 |  1.00659  | 0.315721  | PASS     | spread_proxy   |
| christoffersen_independence |          nan |     nan |  0.236608 | 0.626667  | PASS     | spread_proxy   |
| kupiec_pof                  |            8 |     550 |  1.00659  | 0.315721  | PASS     | aggregate      |
| christoffersen_independence |          nan |     nan |  0.236608 | 0.626667  | PASS     | aggregate      |

## P&L attribution proxy summary

|   pla_proxy_correlation |   pla_proxy_rmse |   actual_pnl_std |   unexplained_share |   actual_on_explained_slope | status   |   residual_risk_budget | claim_boundary                                            |
|------------------------:|-----------------:|-----------------:|--------------------:|----------------------------:|:---------|-----------------------:|:----------------------------------------------------------|
|                 0.92933 |          3936.44 |          10652.3 |             0.36954 |                    0.979857 | PASS     |                    0.4 | P&L attribution proxy only; not an official FRTB PLA test |

## APL/HPL backtesting proxy comparison

|   apl_recent_250_exceptions |   hpl_recent_250_exceptions |   apl_hpl_exception_gap |   apl_hpl_correlation |   residual_std_share | status   | claim_boundary                                                            |
|----------------------------:|----------------------------:|------------------------:|----------------------:|---------------------:|:---------|:--------------------------------------------------------------------------|
|                           3 |                           4 |                       1 |               0.92933 |             0.369745 | PASS     | APL/HPL backtesting proxy only; not an official FRTB P&L attribution test |

## APL/HPL backtesting summary

| pnl_type   |   n_obs |   exceptions |   exception_rate |   severity_sum |   recent_250_obs |   recent_250_exceptions |   recent_250_exception_rate |   recent_250_severity_sum | traffic_light_zone   | traffic_light_basis          |
|:-----------|--------:|-------------:|-----------------:|---------------:|-----------------:|------------------------:|----------------------------:|--------------------------:|:---------------------|:-----------------------------|
| APL_proxy  |     550 |            8 |        0.0145455 |        31586.8 |              250 |                       3 |                       0.012 |                   13062.7 | GREEN                | most_recent_250_observations |
| HPL_proxy  |     550 |            7 |        0.0127273 |        34684.2 |              250 |                       4 |                       0.016 |                   16799.5 | GREEN                | most_recent_250_observations |

## P&L attribution component summary

| component        |     mean |      std |       min |      max |
|:-----------------|---------:|---------:|----------:|---------:|
| equity_component | 235.757  |  7598.4  | -22276    | 23416.6  |
| rates_component  | -30.6193 |  1780.63 |  -5261.61 |  5537.72 |
| spread_component | -19.3899 |  3280.97 | -10331.4  | 10463.1  |
| total_explained  | 185.748  | 10103    | -31643    | 36942.9  |
