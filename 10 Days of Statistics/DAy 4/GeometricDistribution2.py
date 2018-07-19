def geoDist(p, n):
    ans = p * (1 - p) ** (n - 1)
    return ans


if __name__ == '__main__':
    a, b = map(float, input().split())
    n = int(input().strip())

    p = a / b
    print(round(sum([geoDist(p, i) for i in range(1, 6)]), 3))
