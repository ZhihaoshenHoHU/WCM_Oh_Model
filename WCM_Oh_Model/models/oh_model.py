import numpy as np

def Oh2004(SM, thr, ks):
    q = 0.095 * (0.13 + np.sin(1.5 * thr))**1.4 * (1 - np.exp(-1.3 * ks**0.9))
    return (0.11 * SM**0.7 * np.cos(thr)**2.2 *
            (1 - np.exp(-0.32 * ks**1.8))) / q


def Oh2004_inverse(sigmaSM, thr, ks):
    q = 0.095 * (0.13 + np.sin(1.5 * thr))**1.4 * (1 - np.exp(-1.3 * ks**0.9))
    return ((sigmaSM * q) /
            (0.11 * np.cos(thr)**2.2 *
             (1 - np.exp(-0.32 * ks**1.8))))**1.42857