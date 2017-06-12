#!/bin/python3

import sys

def twinArrays(ar1, ar2):
    # Store smaller of two starting values with index in ar1MinVal for array 1
    if ar1[0] < ar1[1]:
        ar1MinVal = [ar1[0], 0]
        ar1MinVal2 = [ar1[1], 1]
    else:
        ar1MinVal = [ar1[1], 1]
        ar1MinVal2 = [ar1[0], 0]

    # Do the same for array 2 
    if ar2[0] < ar2[1]:
        ar2MinVal = [ar2[0], 0]
        ar2MinVal2 = [ar2[1], 1]
    else:
        ar2MinVal = [ar2[1], 1]
        ar2MinVal2 = [ar2[0], 0]

    # Loop through array one in order to find its minimum value w/ index, and the 2nd to smallest value w/ index
    for i in range(2, len(ar1)):
        if ar1[i] < ar1MinVal[0]:
            ar1MinVal2 = ar1MinVal
            ar1MinVal = [ar1[i], i]
        elif ar1[i] < ar1MinVal2[0]:
            ar1MinVal2 = [ar1[i], i]

    # Do the same with array 2 
    for i in range(2, len(ar2)):
        if ar2[i] < ar2MinVal[0]:
            ar2MinVal2 = ar2MinVal
            ar2MinVal = [ar2[i], i]
        elif ar2[i] < ar2MinVal2[0]:
            ar2MinVal2 = [ar2[i], i]

    if ar1MinVal[1] == ar2MinVal[1]:
        sum1 = ar1MinVal2[0] + ar2MinVal[0]
        sum2 = ar1MinVal[0] + ar2MinVal2[0]
        return min(sum1, sum2)
    else:
        return ar1MinVal[0] + ar2MinVal[0]

n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
result = twinArrays(ar1, ar2)
print(result)
