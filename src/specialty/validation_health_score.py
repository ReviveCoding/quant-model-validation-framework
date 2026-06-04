import pandas as pd


def build_validation_health_score(findings_df):
    weights = {'LOW': 3, 'MEDIUM': 8, 'HIGH': 18, 'CRITICAL': 35}
    penalty = sum(weights.get(row.severity, 5) for _, row in findings_df.iterrows())
    score = max(0, 100 - penalty)
    if score >= 80:
        decision = 'PASS'
    elif score >= 60:
        decision = 'REVIEW'
    else:
        decision = 'BLOCK'
    return pd.DataFrame([{'validation_health_score': score, 'finding_penalty': penalty, 'health_decision': decision}])
