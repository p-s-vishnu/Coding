import math

def nChooseX(n,x):
    return math.factorial(n) / (math.factorial(n-x) * math.factorial(x))

def binomial(p,n,x):
    q   = 1 - p
    return nChooseX(6,x)* p**x * q**(n-x)

a,b  = map(float, input().strip().split())

p    = a / (a + b)
ans  = sum([binomial(p,6,i) for i in range(3,7)])
print(round(ans,3))
