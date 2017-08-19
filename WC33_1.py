#!/bin/python3

# https://www.hackerrank.com/contests/w33/challenges/twin-arrays

# You are given two arrays A and B each containing n integers.
# You need to choose exactly one number from A and exactly one number from B
# such that the index of the two chosen numbers is not same
# and the sum of the 2 chosen values is minimum.

# Your objective is to find and print this minimum value.

# My approach for solving this:

# The optimal solution is taking the minimum value from each list.
# The only time when we cannot do this is if they have the same index.
# If they do have the same index, then we either want:
# minimum (first array) + 2nd minimum (second array)
# or
# 2nd minimum (first array) + minimum (second array)

import sys

def twin_arrays(ar1, ar2):
    '''
    Finds an integer in ar1 and ar2 such that their sum is minimum,
    and their indeces are different.
    '''
    # Store smaller of two starting values with index in ar1MinVal for array 1
    if ar1[0] < ar1[1]:
        ar1_min_val = [ar1[0], 0]
        ar1_min_val2 = [ar1[1], 1]
    else:
        ar1_min_val = [ar1[1], 1]
        ar1_min_val2 = [ar1[0], 0]

    # Do the same for array 2
    if ar2[0] < ar2[1]:
        ar2_min_val = [ar2[0], 0]
        ar2_min_val2 = [ar2[1], 1]
    else:
        ar2_min_val = [ar2[1], 1]
        ar2_min_val2 = [ar2[0], 0]

    # Loop through array one in order to find its minimum value w/ index,
    # and the 2nd to smallest value w/ index
    for i in range(2, len(ar1)):
        if ar1[i] < ar1_min_val[0]:
            ar1_min_val2 = ar1_min_val
            ar1_min_val = [ar1[i], i]
        elif ar1[i] < ar1_min_val2[0]:
            ar1_min_val2 = [ar1[i], i]

    # Do the same with array 2
    for i in range(2, len(ar2)):
        if ar2[i] < ar2_min_val[0]:
            ar2_min_val2 = ar2_min_val
            ar2_min_val = [ar2[i], i]
        elif ar2[i] < ar2_min_val2[0]:
            ar2_min_val2 = [ar2[i], i]

    if ar1_min_val[1] == ar2_min_val[1]:
        sum1 = ar1_min_val2[0] + ar2_min_val[0]
        sum2 = ar1_min_val[0] + ar2_min_val2[0]
        return min(sum1, sum2)
    else:
        return ar1_min_val[0] + ar2_min_val[0]

n = int(input().strip())
array_1 = list(map(int, input().strip().split(' ')))
array_2 = list(map(int, input().strip().split(' ')))
result = twin_arrays(array_1, array_2)
print(result)
