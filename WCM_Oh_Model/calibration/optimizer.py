import numpy as np
from scipy.optimize import curve_fit, differential_evolution
from models.oh_model import Oh2004
from models.wcm_model import fitFunc

def error_func(params, SM, thr, ks, sigma0, VI):
    pred = fitFunc((sigma0, VI), *params)
    obs = Oh2004(SM, thr, ks)
    return np.sqrt(np.mean((pred - obs) ** 2))


def optimize_params(SM, thr, ks, sigma0, VI):
    bounds = [
        (0, 1),
        (-1, 0.1),
        (-200, -200),
        (-200, -200)
    ]

    result = differential_evolution(
        error_func,
        bounds,
        args=(SM, thr, ks, sigma0, VI),
        seed=42
    )

    params, _ = curve_fit(
        fitFunc,
        (sigma0, VI),
        Oh2004(SM, thr, ks),
        p0=result.x,
        maxfev=100000
    )

    return params