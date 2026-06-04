import numpy as np
from scipy.stats import chi2


def christoffersen_independence_test(exception_flags):
    flags = np.asarray(exception_flags, dtype=int)
    if len(flags) < 2 or flags.sum() == 0:
        return {'test': 'christoffersen_independence', 'lr_stat': 0.0, 'p_value': 1.0, 'status': 'PASS'}
    n00 = n01 = n10 = n11 = 0
    for a, b in zip(flags[:-1], flags[1:]):
        if a == 0 and b == 0: n00 += 1
        elif a == 0 and b == 1: n01 += 1
        elif a == 1 and b == 0: n10 += 1
        else: n11 += 1
    pi01 = n01 / max(n00+n01, 1)
    pi11 = n11 / max(n10+n11, 1)
    pi = (n01+n11) / max(n00+n01+n10+n11, 1)
    def ll(a,b,p):
        p = min(max(p, 1e-12), 1-1e-12)
        return a*np.log(1-p) + b*np.log(p)
    lr = -2 * ((ll(n00+n10, n01+n11, pi)) - (ll(n00, n01, pi01) + ll(n10, n11, pi11)))
    pval = 1 - chi2.cdf(lr, 1)
    return {'test': 'christoffersen_independence', 'lr_stat': float(lr), 'p_value': float(pval), 'status': 'PASS' if pval >= 0.05 else 'REVIEW'}
