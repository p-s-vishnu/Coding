from math import erf


def cdf(tickets, students, mean, std):
    mean_new = mean * students
    std_new = std * students ** 0.5
    x_input = (tickets - mean_new) / std_new
    return 0.5 * (1 + erf(x_input / 2 ** 0.5))


n = 250
x = 100
mean = 2.4
std = 2.0
print(round(cdf(n, x, mean, std), 4))


