import math


def cdf(x):     
    mean = 20
    std = 2
    X = (x - mean) / std
    return 0.5 * (1 + math.erf(X / 2 ** 0.5))


print(round(cdf(19.5), 3))
print(round(cdf(22) - cdf(20), 3))
