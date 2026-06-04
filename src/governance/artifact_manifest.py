import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def artifact_manifest(root: Path) -> pd.DataFrame:
    rows = []
    for root_file in ['README.md', 'PROJECT_CARD.md', 'Makefile', 'pyproject.toml', 'requirements.txt', 'Dockerfile', '.dockerignore', '.gitignore']:
        path = root / root_file
        if path.exists():
            rows.append({
                'artifact': root_file,
                'size_bytes': path.stat().st_size,
                'sha256_12': _sha256(path)[:12],
            })
    for folder in ['configs', 'src', 'scripts', 'tests', 'outputs', 'reports']:
        base = root / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                rows.append({
                    'artifact': str(path.relative_to(root)),
                    'size_bytes': path.stat().st_size,
                    'sha256_12': _sha256(path)[:12],
                })
    return pd.DataFrame(rows)


def run_manifest(root: Path, release_decision: dict, test_status: str = 'not_run_in_pipeline') -> dict:
    return {
        'generated_at_utc': datetime.now(timezone.utc).isoformat(),
        'project': 'quant_model_validation_framework_final',
        'run_command': 'python scripts/run_pipeline.py',
        'test_command': 'pytest -q',
        'test_status_at_pipeline_time': test_status,
        'release_decision': release_decision,
        'claim_boundary': 'offline synthetic/public-data-sample validation framework; non-production; not regulatory-capital compliant',
    }
