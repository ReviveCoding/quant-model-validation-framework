# Pricing Validation Report

Generated: 2026-06-04

## Benchmark summary

|        |    abs_error |   rel_abs_error | gate   |
|:-------|-------------:|----------------:|:-------|
| count  |  80          |     80          | 80     |
| unique | nan          |    nan          | 2      |
| top    | nan          |    nan          | PASS   |
| freq   | nan          |    nan          | 76     |
| mean   |   0.234914   |      0.016423   | nan    |
| std    |   0.264059   |      0.0171364  | nan    |
| min    |   0.00174807 |      0.00014016 | nan    |
| 25%    |   0.0608203  |      0.00527548 | nan    |
| 50%    |   0.130977   |      0.0111213  | nan    |
| 75%    |   0.333529   |      0.0204209  | nan    |
| max    |   1.53963    |      0.0867919  | nan    |

## No-arbitrage checks

| check                  |   violations | status   |
|:-----------------------|-------------:|:---------|
| call_lower_upper_bound |            0 | PASS     |

## Residual error correction

|   baseline_mae |   corrected_mae |   relative_mae_reduction | residual_model          |
|---------------:|----------------:|-------------------------:|:------------------------|
|       0.234914 |        0.237809 |               -0.0123211 | closed_form_numpy_ridge |
