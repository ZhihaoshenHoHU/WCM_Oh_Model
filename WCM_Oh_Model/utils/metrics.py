import numpy as np

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))


def correlation(y_true, y_pred):
    return np.corrcoef(y_true, y_pred)[0, 1]