def findMedian(inputList):
    n   = len(inputList)
    mid = int(n/2)
    if(n % 2 == 0 ):
        return (inputList[mid-1] + inputList[mid]) / 2
    else:
        return inputList[mid]

if __name__ == '__main__':
    n           = int(input())
    mid         = int(n/2)
    inputList   = sorted([int(num) for num in input().split()])

    q2      = findMedian(inputList)
    q1      = findMedian(inputList[: mid] )
    if(n%2 == 0):
        q3      = findMedian(inputList[mid:n])
    else:
        q3      = findMedian(inputList[mid+1 : n])
    # Constraint given Q1 Q2 Q3 will be integers
    print(int(q1))
    print(int(q2))
    print(int(q3))
