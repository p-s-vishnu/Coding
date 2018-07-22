from math import erf


def cdf(x, n, mean, std):
    mean_new = mean * n
    std_new = std * n ** 0.5
    x_input = (x - mean_new) / std_new
    return 0.5 * (1 + erf(x_input / 2 ** 0.5))


n = 49
mean = 205
std = 15
print(round(cdf(9800, n, mean, std), 4))
