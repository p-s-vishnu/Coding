def rank(l):
    return [sorted(l).index(i) for i in l]


n = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))

rank_x = rank(x)
rank_y = rank(y)
d2 = [ (xi - yi)**2 for (xi, yi) in list(zip(rank_x,rank_y)) ]
r = 1 - 6* sum(d2)/ (n**3 - n)

print(round(r,3))
