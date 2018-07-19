import math


def nChooseX(n, x):
    return math.factorial(n) / (math.factorial(n - x) * math.factorial(x))


def binomial(p, n, x):
    q = 1 - p
    return nChooseX(n, x) * p ** x * q ** (n - x)


a, n = map(int, input().strip().split())
p = float(a) / 100

ans1 = sum([binomial(p, n, i) for i in range(3)])
ans2 = sum([binomial(p, n, i) for i in range(2, n + 1)])
print(round(ans1, 3))
print(round(ans2, 3))
