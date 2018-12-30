#!/bin/python3

'''
Given lists A and B, find the pair (x,y) such that

1. x is in A, y is in B
2. gcd(x,y) is the maximum out of all pairs (x,y)
3. If there is a tie for the gcd, pick the pair with the greatest sum.

After you have found this pair, return the sum.
'''

def maximumGcdAndSum(A, B):
    ''' TODO '''

    #We know that we cannot have a GCD higher than the maximum of a set
    max_a, max_b = max(A), max(B)
    maximum_possible_factor = min(max_a, max_b)
    highest_val = max(max_a, max_b)

    A = set(A)
    B = set(B)

    #We are going to start with the highest possible GCD and work our way down
    for possible_gcd in range(maximum_possible_factor, 0, -1):

        #For this given GCD to be our answer, it has to have a multiple in A and a multiple in B
        x = possible_gcd * (highest_val // possible_gcd)
        fnum = 0
        snum = 0
        while x >= 1:
            if fnum == 0:
                if x in A:
                    fnum = x
            if snum == 0:
                if x in B:
                    snum = x
            #We are going through each possible multiple of the GCD that will fit in the set
            x -= possible_gcd

        if fnum != 0 and snum != 0:
            return fnum + snum

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    print(maximumGcdAndSum(A, B))
