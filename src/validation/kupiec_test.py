import math
from scipy.stats import chi2


def kupiec_pof_test(exceptions, n_obs, alpha=0.99):
    x = int(exceptions)
    p = 1 - alpha
    if n_obs <= 0:
        return {'test': 'kupiec_pof', 'exceptions': x, 'n_obs': n_obs, 'lr_stat': None, 'p_value': None, 'status': 'REVIEW'}
    phat = x / n_obs
    if x == 0:
        lr = -2 * (n_obs * math.log(1 - p) - n_obs * math.log(max(1 - phat, 1e-12)))
    elif x == n_obs:
        lr = -2 * (x * math.log(p) - x * math.log(phat))
    else:
        lr = -2 * ((n_obs-x)*math.log(1-p) + x*math.log(p) - ((n_obs-x)*math.log(1-phat) + x*math.log(phat)))
    pval = 1 - chi2.cdf(lr, 1)
    return {'test': 'kupiec_pof', 'exceptions': x, 'n_obs': n_obs, 'lr_stat': lr, 'p_value': pval, 'status': 'PASS' if pval >= 0.05 else 'REVIEW'}
