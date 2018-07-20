[mu1, mu2] = [float(i) for i in input().split()]

# cost of A
print(round(160 + 40 * (mu1 + mu1 ** 2), 3))

# cost of B
print(round(128 + 40 * (mu2 + mu2 ** 2), 3))
