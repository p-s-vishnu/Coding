def mean(list):
    return sum(list) / len(list)

def stdDev(list):
    mu      = mean(list)
    n       = len(list)
    var     = sum( [(x-mu)**2 for x in list] )/n
    return var**(1/2)

n = int(input())
x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

x_mean = mean(x)
y_mean = mean(y)
x_sigma = stdDev(x)
y_sigma = stdDev(y)

covariance = sum([(xi - x_mean)*(yi - y_mean) for xi,yi in zip(x,y)])/n

print(round(covariance / ( x_sigma * y_sigma),3))
