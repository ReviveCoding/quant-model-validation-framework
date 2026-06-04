from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_operational_replay_generates_outputs():
    result = subprocess.run(
        [sys.executable, "scripts/run_operational_replay.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert (ROOT / "outputs" / "operational_replay_log.csv").exists()
    assert (ROOT / "outputs" / "recalibration_summary.csv").exists()
    assert (ROOT / "reports" / "operational_replay_report.md").exists()
    assert (ROOT / "reports" / "model_operations_runbook.md").exists()
