import math


def poisson(l, k):
    numerator = lam ** k * math.e ** -l
    return numerator / math.factorial(k)


lam = float(input())
K = int(input())

print(round(poisson(lam, K), 3))
