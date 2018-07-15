if __name__ == '__main__':
    n = int(input())
    inputNum = [int(i) for i in input().split()]
    weights  = [int(w) for w in input().split()]

    wiSum   = 0
    wSum    = 0
    for i,w in zip(inputNum,weights):
        wiSum   += i*w
        wSum    += w

    print( round(wiSum / wSum , 1) )
