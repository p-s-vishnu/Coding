import math


def normalDis(x):
    mean = 20
    std = 2
    X = (x - mean) / std
    return 0.5 * (1 + math.erf(X / 2 ** 0.5))


print(round(normalDis(19.5), 3))
print(round(normalDis(22) - normalDis(20), 3))
