n = 100
mean = 500  # mean of the sample is the mean of the population
std_ = 80
std = std_ / n ** 0.5  # population standard deviation into the sample standard deviation

z = 1.96
print(round(mean - std * z, 2))
print(round(mean + std * z, 2))
