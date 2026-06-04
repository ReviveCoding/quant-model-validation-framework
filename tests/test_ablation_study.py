from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def test_ablation_study_generates_resume_metrics():
    result = subprocess.run(
        [sys.executable, "scripts/run_ablation_study.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert (ROOT / "outputs" / "baseline_vs_enhanced_ablation.csv").exists()
    assert (ROOT / "reports" / "baseline_vs_enhanced_ablation_report.md").exists()
