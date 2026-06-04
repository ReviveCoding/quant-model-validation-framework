from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
REPORTS = ROOT / "reports"


def run_pipeline_once(run_id: int, operating_day: str) -> dict:
    start = time.perf_counter()
    completed = subprocess.run(
        [sys.executable, "scripts/run_pipeline.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    runtime = time.perf_counter() - start

    release_path = OUTPUTS / "release_decision.json"
    health_path = OUTPUTS / "validation_health_scores.csv"
    findings_path = OUTPUTS / "model_risk_findings.csv"
    backtest_path = OUTPUTS / "backtesting_summary.csv"

    release = json.loads(release_path.read_text(encoding="utf-8")) if release_path.exists() else {}
    health = pd.read_csv(health_path) if health_path.exists() else pd.DataFrame()
    findings = pd.read_csv(findings_path) if findings_path.exists() else pd.DataFrame()
    backtest = pd.read_csv(backtest_path) if backtest_path.exists() else pd.DataFrame()

    health_score = float(health["validation_health_score"].iloc[0]) if "validation_health_score" in health.columns and len(health) else np.nan
    final_false_pass = float(health["false_pass_rate"].iloc[0]) if "false_pass_rate" in health.columns and len(health) else np.nan

    high_or_critical = 0
    if len(findings) and "severity" in findings.columns:
        high_or_critical = int(findings["severity"].isin(["HIGH", "CRITICAL"]).sum())

    recent_250_exceptions = np.nan
    traffic_light_zone = "UNKNOWN"
    if len(backtest):
        if "recent_250_exceptions" in backtest.columns:
            recent_250_exceptions = float(backtest["recent_250_exceptions"].iloc[0])
        if "traffic_light_zone" in backtest.columns:
            traffic_light_zone = str(backtest["traffic_light_zone"].iloc[0])

    status = release.get("release_decision", release.get("decision", "UNKNOWN"))

    recalibration_trigger = (
        status in {"REVIEW", "BLOCK"}
        or high_or_critical > 0
        or (not np.isnan(health_score) and health_score < 85)
        or (not np.isnan(final_false_pass) and final_false_pass > 0)
        or traffic_light_zone in {"YELLOW", "RED"}
    )

    return {
        "run_id": run_id,
        "operating_day": operating_day,
        "return_code": completed.returncode,
        "runtime_seconds": round(runtime, 4),
        "release_decision": status,
        "validation_health_score": health_score,
        "false_pass_rate": final_false_pass,
        "high_or_critical_findings": high_or_critical,
        "recent_250_exceptions": recent_250_exceptions,
        "traffic_light_zone": traffic_light_zone,
        "recalibration_trigger": bool(recalibration_trigger),
        "stdout_tail": completed.stdout[-300:],
        "stderr_tail": completed.stderr[-300:],
    }


def build_recalibration_summary(log: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "num_operating_runs": len(log),
                "pass_rate": round((log["release_decision"] == "PASS").mean(), 4),
                "review_or_block_rate": round(log["release_decision"].isin(["REVIEW", "BLOCK"]).mean(), 4),
                "recalibration_trigger_rate": round(log["recalibration_trigger"].mean(), 4),
                "avg_runtime_seconds": round(log["runtime_seconds"].mean(), 4),
                "max_runtime_seconds": round(log["runtime_seconds"].max(), 4),
                "avg_validation_health_score": round(log["validation_health_score"].mean(), 4),
                "min_validation_health_score": round(log["validation_health_score"].min(), 4),
                "max_recent_250_exceptions": round(log["recent_250_exceptions"].max(), 4),
            }
        ]
    )


def write_reports(log: pd.DataFrame, summary: pd.DataFrame) -> None:
    REPORTS.mkdir(exist_ok=True, parents=True)

    report = [
        "# Operational Replay & Recalibration Experiment",
        "",
        "This experiment simulates repeated local operating-day validation runs for the quant model validation framework.",
        "It is a non-production, synthetic/public-sample operational replay designed to test run repeatability, release-gate stability, monitoring behavior, and recalibration triggers.",
        "",
        "## Summary",
        "",
        summary.to_markdown(index=False),
        "",
        "## Operating Run Log",
        "",
        log[
            [
                "run_id",
                "operating_day",
                "runtime_seconds",
                "release_decision",
                "validation_health_score",
                "false_pass_rate",
                "recent_250_exceptions",
                "traffic_light_zone",
                "recalibration_trigger",
            ]
        ].to_markdown(index=False),
        "",
        "## Interpretation",
        "",
        "- PASS across repeated runs indicates stable local/GitHub runnable behavior.",
        "- A recalibration trigger does not imply production model failure; it flags conditions that would require review in a model-risk workflow.",
        "- This is not a regulatory capital engine and should be described as a synthetic/public-sample operational replay.",
    ]

    (REPORTS / "operational_replay_report.md").write_text("\n".join(report), encoding="utf-8")

    runbook = [
        "# Model Operations Runbook",
        "",
        "## Purpose",
        "Provide a lightweight operating procedure for running the non-production quant model validation framework.",
        "",
        "## Standard Run",
        "```bash",
        "python scripts/run_pipeline.py",
        "python -m pytest -q",
        "python scripts/evaluate_performance.py",
        "python scripts/run_operational_replay.py",
        "```",
        "",
        "## Review Triggers",
        "- Release decision is REVIEW or BLOCK.",
        "- Validation health score drops below 85.",
        "- False-pass rate is above 0.",
        "- High or critical model-risk findings appear.",
        "- Recent 250-day traffic-light zone is YELLOW or RED.",
        "",
        "## Escalation",
        "Document the breach, inspect model-risk findings, compare champion/challenger outputs, rerun assumption sensitivity, and record compensating controls.",
        "",
        "## Claim Boundary",
        "This runbook supports a local, synthetic/public-sample, non-production validation project. It does not claim production trading, official regulatory capital, or bank-approved model use.",
    ]

    (REPORTS / "model_operations_runbook.md").write_text("\n".join(runbook), encoding="utf-8")


def main() -> None:
    OUTPUTS.mkdir(exist_ok=True, parents=True)
    REPORTS.mkdir(exist_ok=True, parents=True)

    operating_days = pd.date_range("2026-06-01", periods=5, freq="B")
    rows = []

    for i, day in enumerate(operating_days, start=1):
        rows.append(run_pipeline_once(i, str(day.date())))

    log = pd.DataFrame(rows)
    summary = build_recalibration_summary(log)

    log.to_csv(OUTPUTS / "operational_replay_log.csv", index=False)
    summary.to_csv(OUTPUTS / "recalibration_summary.csv", index=False)
    write_reports(log, summary)

    status = "PASS" if (log["return_code"].eq(0).all() and summary["pass_rate"].iloc[0] >= 0.8) else "REVIEW"

    print("Operational replay completed.")
    print(f"Status: {status}")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
