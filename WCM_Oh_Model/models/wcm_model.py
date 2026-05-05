import numpy as np

def fitFunc(X, a, b, g, h):
    sigma0, VI = X
    return (sigma0 - a*(g*VI + h)*0.788*(1 - np.exp(-2*b*(g*VI + h)/0.788))) \
           * np.exp(2*b*(g*VI + h)/0.788)


def fitFunc2(VI, a, b, g, h):
    return a*(g*VI + h)*0.788*(1 - np.exp(-2*b*(g*VI + h)/0.788))


def fitFunc3(X, a, b, g, h):
    sigmaSM, VI = X
    K = np.exp(2*b*(g*VI + h)/0.788)
    return (sigmaSM + a*(g*VI + h)*0.788*(K - 1)) / K