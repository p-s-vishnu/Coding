from itertools import product

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
          
l   = [l1, l2]
ans = list(product(*l))
for a in ans:
    print(a, end=' ')

    
# from itertools import product

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# print(*product(a, b))