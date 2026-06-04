# Numerical Reliability Report

Generated: 2026-06-04

## Convergence summary

| test                 |   grid |    price |   benchmark |   abs_error |     stderr |   ci_covers_benchmark |
|:---------------------|-------:|---------:|------------:|------------:|-----------:|----------------------:|
| binomial_convergence |     25 | 11.4438  |     11.3485 |  0.0953192  | nan        |                   nan |
| binomial_convergence |     50 | 11.2993  |     11.3485 |  0.0492159  | nan        |                   nan |
| binomial_convergence |    100 | 11.3238  |     11.3485 |  0.0246399  | nan        |                   nan |
| binomial_convergence |    200 | 11.3361  |     11.3485 |  0.0123278  | nan        |                   nan |
| binomial_convergence |    400 | 11.3423  |     11.3485 |  0.00616585 | nan        |                   nan |
| mc_convergence       |   1000 |  9.44161 |     11.3485 |  1.90687    |   0.502244 |                     0 |
| mc_convergence       |   2500 | 10.6959  |     11.3485 |  0.652608   |   0.350042 |                     1 |
| mc_convergence       |   5000 | 11.0018  |     11.3485 |  0.346687   |   0.249686 |                     1 |
| mc_convergence       |  10000 | 11.076   |     11.3485 |  0.272522   |   0.176729 |                     1 |
| mc_convergence       |  20000 | 11.1442  |     11.3485 |  0.204323   |   0.124841 |                     1 |

## Seed stability

|   seed |   price |   stderr |   price_std_across_seeds |   relative_std |
|-------:|--------:|---------:|-------------------------:|---------------:|
|      7 | 11.076  | 0.176729 |                 0.206738 |      0.0182336 |
|     11 | 11.5539 | 0.179947 |                 0.206738 |      0.0182336 |
|     19 | 11.3743 | 0.180446 |                 0.206738 |      0.0182336 |
|     23 | 11.1789 | 0.176802 |                 0.206738 |      0.0182336 |
|     31 | 11.5084 | 0.180883 |                 0.206738 |      0.0182336 |

## CPU/GPU consistency boundary

| check               |   cpu_value | gpu_value   | relative_error   | status   |
|:--------------------|------------:|:------------|:-----------------|:---------|
| cpu_gpu_consistency |     17.8992 |             |                  | NOT_RUN  |
