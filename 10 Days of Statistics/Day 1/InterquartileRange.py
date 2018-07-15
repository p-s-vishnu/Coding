def findMedian(inputList):
    n   = len(inputList)
    mid = n//2
    if(n % 2 == 0 ):
        return (inputList[mid-1] + inputList[mid]) / 2
    else:
        return inputList[mid]

def getIQR(list):
    n       = len(list)
    mid     = n//2      # floor of length

    q1      = findMedian(list[: mid] )
    if(n%2 == 0):
        q3      = findMedian(list[mid:])
    else:
        q3      = findMedian(list[mid+1 :])

    return round(float(q3 - q1),1)

n       = int(input())
elem    = [e for e in input().split()]
freq    = [int(f) for f in input().split()]
combined= []
for e,f in zip(elem,freq):
    for i in range(f):
        combined.append(int(e))

combined.sort()
print(getIQR(combined))
