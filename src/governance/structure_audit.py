from pathlib import Path
import pandas as pd


def structure_audit(root: Path):
    required = [
        'README.md', 'PROJECT_CARD.md', 'Makefile', 'pyproject.toml', 'requirements.txt', '.gitignore',
        'Dockerfile', '.dockerignore', '.github/workflows/ci.yml', 'scripts/run_pipeline.py', 'tests', 'src', 'configs', 'outputs', 'reports'
    ]
    rows = []
    for rel in required:
        p = root / rel
        rows.append({'item': rel, 'exists': p.exists(), 'type': 'dir' if p.is_dir() else 'file'})
    # Identify heavy/cache artifacts that should not be committed.
    risky_patterns = ['.pytest_cache', '__pycache__', '.venv', 'venv', '.ipynb_checkpoints']
    risky = []
    for pattern in risky_patterns:
        risky.extend([str(p.relative_to(root)) for p in root.rglob(pattern) if p.exists()])
    return pd.DataFrame(rows), pd.DataFrame({'non_github_artifact': risky}) if risky else pd.DataFrame(columns=['non_github_artifact'])
