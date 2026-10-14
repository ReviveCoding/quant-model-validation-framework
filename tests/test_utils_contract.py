"""File helper contracts use temporary directories and preserve path semantics."""

import json

import pandas as pd

from utils import load_yaml, project_path, write_csv, write_json, write_md


def test_project_path_resolves_relative_and_absolute(tmp_path):
    assert project_path("reports", "result.json") == project_path() / "reports/result.json"
    assert project_path(tmp_path, "absolute.json") == tmp_path / "absolute.json"


def test_file_helpers_create_parent_directories(tmp_path):
    payload = {"status": "ok", "count": 2}
    output = tmp_path / "nested"
    write_json(output / "result.json", payload)
    write_md(output / "summary.md", "# Summary\n")
    write_csv(output / "scores.csv", pd.DataFrame({"score": [0.2, 0.7]}))
    assert json.loads((output / "result.json").read_text(encoding="utf-8")) == payload
    assert (output / "summary.md").read_text(encoding="utf-8") == "# Summary\n"
    assert pd.read_csv(output / "scores.csv")["score"].tolist() == [0.2, 0.7]


def test_load_yaml_from_absolute_path(tmp_path):
    config = tmp_path / "configuration.yaml"
    config.write_text("enabled: true\nthreshold: 0.25\n", encoding="utf-8")
    assert load_yaml(config) == {"enabled": True, "threshold": 0.25}
