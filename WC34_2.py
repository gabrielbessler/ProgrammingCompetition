#!/bin/python3

import sys

def maximumGcdAndSum(A, B):

    #We know that we cannot have a GCD higher than the maximum of a set
    maximum_possible_factor = min(max(A), max(B))
    highest_val = max(max(A), max(B))

    #We are going to start with the highest possible GCD and work our way down
    for possible_gcd in range(maximum_possible_factor, 0, -1):

        #For this given GCD to be our answer, it has to have a multiple in A and a multiple in B
        x = possible_gcd
        fnum = 0
        snum = 0
        while x <= highest_val:
            if x in A:
                fnum = x
            if x in B:
                snum = x
            #We are going through each possible multiple of the GCD that will fit in the set
            x += possible_gcd

        if fnum != 0 and snum != 0:
            return (fnum + snum)

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    print(maximumGcdAndSum(A, B))
