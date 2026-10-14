from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]


def project_path(*parts: str | Path) -> Path:
    """Resolve paths against the repository root, retaining absolute overrides."""
    return ROOT.joinpath(*parts)


def ensure_dirs() -> None:
    for directory in ("data/public", "data/synthetic", "data/processed", "outputs", "reports"):
        project_path(directory).mkdir(parents=True, exist_ok=True)


def load_yaml(rel: str | Path):
    return yaml.safe_load(project_path(rel).read_text(encoding="utf-8"))


def write_json(rel: str | Path, obj: object) -> None:
    path = project_path(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def write_md(rel: str | Path, content: str) -> None:
    path = project_path(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def write_csv(rel: str | Path, df: pd.DataFrame) -> None:
    path = project_path(rel)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
