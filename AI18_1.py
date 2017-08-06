#!/bin/python3

import sys
import math

'''
Problem Statement

You have been given an integer  which represents the length of one of cathetus of a right-angle triangle.
You need to find the lengths of the remaining sides. There may be multiple possible answers; any one will be accepted.
'''

def pythagoreanTriple(side_length):
    ''' '''

    if side_length % 2 == 1: #a is odd
        k = (side_length - 1) // 2
        b = 2*(k+1)*k
        c = (k+1)**2 + k**2
        return int(side_length), int(b), int(c)
    else: #a is even
        num_div = 0
        while side_length % 2 != 1:
            side_length //= 2
            num_div += 1
        if side_length == 1: # this means a was a power of 2
            side_length *= (2 ** num_div)
            multiple = side_length // 4
            return int(side_length), int(3 * multiple), int(5 * multiple)
        else:
            k = (side_length - 1) // 2
            b = 2*(k+1)*k
            c = (k+1)**2 + k**2
            mul = 2 ** num_div
            return int(side_length * mul), int(b*mul), int(c*mul)

# Integer division is required (floating point math is annoying)

a = int(input().strip())
triple = pythagoreanTriple(a)
print(" ".join(map(str, triple)))
