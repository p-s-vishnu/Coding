def mean(list):
    return sum(list) / len(list)

def stdDev(list):
    mu      = mean(list)
    n       = len(list)
    var     = sum( [(x-mu)**2 for x in list] )/n
    return var**(1/2)

n       = int(input())
list    = [int(x) for x in input().split()]
print(round(stdDev(list),1))
