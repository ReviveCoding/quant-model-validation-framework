# Operational Replay & Recalibration Experiment

This experiment simulates repeated local operating-day validation runs for the quant model validation framework.
It is a non-production, synthetic/public-sample operational replay designed to test run repeatability, release-gate stability, monitoring behavior, and recalibration triggers.

## Summary

|   num_operating_runs |   pass_rate |   review_or_block_rate |   recalibration_trigger_rate |   avg_runtime_seconds |   max_runtime_seconds |   avg_validation_health_score |   min_validation_health_score |   max_recent_250_exceptions |
|---------------------:|------------:|-----------------------:|-----------------------------:|----------------------:|----------------------:|------------------------------:|------------------------------:|----------------------------:|
|                    5 |           1 |                      0 |                            0 |                2.7038 |                 2.735 |                            92 |                            92 |                           3 |

## Operating Run Log

|   run_id | operating_day   |   runtime_seconds | release_decision   |   validation_health_score |   false_pass_rate |   recent_250_exceptions | traffic_light_zone   | recalibration_trigger   |
|---------:|:----------------|------------------:|:-------------------|--------------------------:|------------------:|------------------------:|:---------------------|:------------------------|
|        1 | 2026-06-01      |            2.6108 | PASS               |                        92 |               nan |                       3 | GREEN                | False                   |
|        2 | 2026-06-02      |            2.735  | PASS               |                        92 |               nan |                       3 | GREEN                | False                   |
|        3 | 2026-06-03      |            2.7071 | PASS               |                        92 |               nan |                       3 | GREEN                | False                   |
|        4 | 2026-06-04      |            2.7335 | PASS               |                        92 |               nan |                       3 | GREEN                | False                   |
|        5 | 2026-06-05      |            2.7326 | PASS               |                        92 |               nan |                       3 | GREEN                | False                   |

## Interpretation

- PASS across repeated runs indicates stable local/GitHub runnable behavior.
- A recalibration trigger does not imply production model failure; it flags conditions that would require review in a model-risk workflow.
- This is not a regulatory capital engine and should be described as a synthetic/public-sample operational replay.