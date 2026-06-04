from utils import project_path
from governance.structure_audit import structure_audit


def test_structure_audit_has_core_files():
    req, _ = structure_audit(project_path())
    missing = req.loc[~req['exists'], 'item'].tolist()
    assert not missing
