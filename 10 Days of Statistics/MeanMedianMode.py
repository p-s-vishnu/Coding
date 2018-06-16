if __name__ == '__main__':
    N = int(input())

    #Mean
    inputNum    = [int(num) for num in input().split()]
    print(sum(inputNum)/N)

    #Median
    median = 0
    inputNum.sort()
    if(N%2 == 0):
        mid = int(N/2)
        median    =   (inputNum[ mid - 1] + inputNum[mid])/2
    else:
        median    =   inputNum[math.floor(N/2)]
    print(median)

    #Mode
    print(max(inputNum, key=inputNum.count))
