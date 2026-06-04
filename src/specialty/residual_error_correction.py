import numpy as np
import pandas as pd


def _ridge_predict_closed_form(x_train: np.ndarray, y_train: np.ndarray, x_all: np.ndarray, alpha: float = 1.0) -> np.ndarray:
    """Small deterministic ridge regression helper using NumPy only.

    The project uses this instead of an external estimator to keep CI/Docker validation lightweight
    and avoid nonessential dependency or thread-pool behavior in minimal environments.
    """
    mu = x_train.mean(axis=0)
    sigma = x_train.std(axis=0)
    sigma = np.where(sigma < 1e-12, 1.0, sigma)
    x_train_s = (x_train - mu) / sigma
    x_all_s = (x_all - mu) / sigma
    x_train_design = np.column_stack([np.ones(len(x_train_s)), x_train_s])
    x_all_design = np.column_stack([np.ones(len(x_all_s)), x_all_s])
    penalty = np.eye(x_train_design.shape[1]) * alpha
    penalty[0, 0] = 0.0  # do not penalize intercept
    beta = np.linalg.solve(x_train_design.T @ x_train_design + penalty, x_train_design.T @ y_train)
    return x_all_design @ beta


def residual_error_correction(df, target_col='mc_error'):
    features = df[['moneyness', 'T', 'sigma', 'r']].to_numpy(dtype=float)
    target = df[target_col].to_numpy(dtype=float)
    split = max(int(0.7 * len(df)), 2)
    pred = _ridge_predict_closed_form(features[:split], target[:split], features, alpha=1.0)
    out = df.copy()
    out['residual_correction'] = pred
    out['corrected_error'] = out[target_col] - out['residual_correction']
    if 'bs_price' in out.columns:
        denom = out['bs_price'].abs().clip(lower=1.0)
        out['relative_error'] = out[target_col] / denom
        out['corrected_relative_error'] = out['corrected_error'] / denom
    baseline_mae = float(np.mean(np.abs(out[target_col])))
    corrected_mae = float(np.mean(np.abs(out['corrected_error'])))
    improvement = (baseline_mae - corrected_mae) / max(baseline_mae, 1e-12)
    summary = pd.DataFrame([{
        'baseline_mae': baseline_mae,
        'corrected_mae': corrected_mae,
        'relative_mae_reduction': improvement,
        'residual_model': 'closed_form_numpy_ridge',
    }])
    return out, summary
