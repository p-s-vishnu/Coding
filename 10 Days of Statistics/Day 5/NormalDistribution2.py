import math


def normalDis(x):
    mean = 70
    std = 10
    X = (x - mean) / std
    return 0.5 * (1 + math.erf(X / 2 ** 0.5))


print(round((1 - normalDis(80)) * 100, 2))
print(round((1 - normalDis(60)) * 100, 2))
print(round(normalDis(60) * 100, 2))
