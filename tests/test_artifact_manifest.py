from pathlib import Path
from governance.artifact_manifest import artifact_manifest, run_manifest


def test_artifact_manifest_and_run_manifest():
    root = Path(__file__).resolve().parents[1]
    manifest = artifact_manifest(root)
    assert 'README.md' in set(manifest['artifact'])
    run = run_manifest(root, {'release_decision': 'PASS'})
    assert run['run_command'] == 'python scripts/run_pipeline.py'
