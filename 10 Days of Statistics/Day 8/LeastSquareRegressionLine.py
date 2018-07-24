X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]
n = 5

x_ = sum(X)/n
x2_= sum([x**2 for x in X])/n
y_ = sum(Y)/n
xy_ = sum([x*y for x,y in list(zip(X, Y))])/n

m = (x_*y_ - xy_)/(x_**2 - x2_)
b = y_ - m*x_

# predict marks in statistics if he got 80 in maths(x)
print( round(m*80 + b, 3) )
