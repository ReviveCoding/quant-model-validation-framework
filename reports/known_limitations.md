# Known Limitations

- Uses synthetic portfolios and fallback public-data-shaped samples.
- Does not use proprietary desk positions, transaction data, or validated market-data vendor feeds.
- Heston, Vasicek, and CIR implementations are educational validation benchmarks, not calibrated production pricers.
- FRTB references are diagnostic/inspired only; this project does not claim regulatory compliance.
- CPU/GPU consistency check is implemented as a scaffold and reports NOT_RUN when GPU results are unavailable.
