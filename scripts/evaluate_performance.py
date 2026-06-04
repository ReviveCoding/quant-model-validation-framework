from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
REPORTS = ROOT / "reports"


def run_command(cmd: list[str]) -> dict:
    start = time.perf_counter()
    completed = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    elapsed = time.perf_counter() - start
    return {
        "command": " ".join(cmd),
        "return_code": completed.returncode,
        "runtime_seconds": round(elapsed, 4),
        "stdout_tail": completed.stdout[-1000:],
        "stderr_tail": completed.stderr[-1000:],
    }


def folder_stats(path: Path) -> dict:
    files = [p for p in path.rglob("*") if p.is_file()]
    total_bytes = sum(p.stat().st_size for p in files)
    largest = max(files, key=lambda p: p.stat().st_size, default=None)
    return {
        "path": str(path.relative_to(ROOT)),
        "file_count": len(files),
        "total_kb": round(total_bytes / 1024, 2),
        "largest_file": str(largest.relative_to(ROOT)) if largest else None,
        "largest_file_kb": round(largest.stat().st_size / 1024, 2) if largest else 0,
    }


def main() -> None:
    results = {
        "purpose": "Lightweight local/GitHub runtime and artifact audit for the quant model validation framework.",
        "python_executable": sys.executable,
        "pipeline": run_command([sys.executable, "scripts/run_pipeline.py"]),
        "pytest": run_command([sys.executable, "-m", "pytest", "-q"]),
        "outputs": folder_stats(OUTPUTS),
        "reports": folder_stats(REPORTS),
    }

    pass_fail = (
        results["pipeline"]["return_code"] == 0
        and results["pytest"]["return_code"] == 0
        and results["outputs"]["file_count"] > 0
        and results["reports"]["file_count"] > 0
    )
    results["performance_eval_status"] = "PASS" if pass_fail else "REVIEW"

    out_json = OUTPUTS / "performance_evaluation_summary.json"
    out_md = REPORTS / "performance_evaluation_report.md"

    out_json.write_text(json.dumps(results, indent=2), encoding="utf-8")

    out_md.write_text(
        "# Performance Evaluation Report\n\n"
        "This lightweight evaluation checks local/GitHub runnable behavior, runtime, and generated artifact footprint. "
        "It is not a production latency benchmark.\n\n"
        f"- Status: **{results['performance_eval_status']}**\n"
        f"- Pipeline runtime seconds: {results['pipeline']['runtime_seconds']}\n"
        f"- Pytest runtime seconds: {results['pytest']['runtime_seconds']}\n"
        f"- Output artifact count: {results['outputs']['file_count']}\n"
        f"- Report artifact count: {results['reports']['file_count']}\n"
        f"- Output footprint KB: {results['outputs']['total_kb']}\n"
        f"- Report footprint KB: {results['reports']['total_kb']}\n"
        f"- Largest output file: {results['outputs']['largest_file']} ({results['outputs']['largest_file_kb']} KB)\n",
        encoding="utf-8",
    )

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
