import math


def nCr(n, r):
    return math.factorial(n) / (math.factorial(n - r) * math.factorial(r))


def negDist(p, n, x):
    # type: (float, int, int) -> float
    ans = nCr(n - 1, x - 1) * p ** x * (1 - p) ** (n - x)
    return round(ans, 3)


if __name__ == '__main__':
    a, b = map(float, input().split())
    n = int(input().strip())

    p = a / b
    print(negDist(p, n, 1))
