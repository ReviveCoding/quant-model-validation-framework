from pathlib import Path
import json
import yaml
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def project_path(*parts):
    return ROOT.joinpath(*parts)

def ensure_dirs():
    for d in ['data/public', 'data/synthetic', 'data/processed', 'outputs', 'reports']:
        project_path(d).mkdir(parents=True, exist_ok=True)

def load_yaml(rel):
    with open(project_path(rel), 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def write_json(rel, obj):
    p = project_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, indent=2), encoding='utf-8')

def write_md(rel, content):
    p = project_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

def write_csv(rel, df):
    p = project_path(rel)
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p, index=False)
