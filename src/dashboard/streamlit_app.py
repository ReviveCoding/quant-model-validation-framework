from pathlib import Path
import json
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
st.title('Quant Model Validation Framework Dashboard')

for rel in ['outputs/release_decision.json', 'outputs/validation_health_scores.csv', 'outputs/model_risk_findings.csv', 'outputs/kupiec_christoffersen_results.csv']:
    path = ROOT / rel
    st.subheader(rel)
    if path.exists():
        if path.suffix == '.json':
            st.json(json.loads(path.read_text()))
        else:
            st.dataframe(pd.read_csv(path))
    else:
        st.warning(f'{rel} not found. Run python scripts/run_pipeline.py first.')
