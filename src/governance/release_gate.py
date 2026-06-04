import json


def release_decision(health_score, findings_df, false_pass_rate=0.0):
    critical = int((findings_df['severity'] == 'CRITICAL').sum())
    high = int((findings_df['severity'] == 'HIGH').sum())
    if critical > 0 or health_score < 60 or false_pass_rate > 0.20:
        decision = 'BLOCK'
    elif high > 0 or health_score < 80 or false_pass_rate > 0.10:
        decision = 'REVIEW'
    else:
        decision = 'PASS'
    return {
        'release_decision': decision,
        'validation_health_score': float(health_score),
        'critical_findings': critical,
        'high_findings': high,
        'false_pass_rate': float(false_pass_rate),
        'claim_boundary': 'offline synthetic/public-data-sample independent validation framework; non-production; not regulatory-capital compliant'
    }
