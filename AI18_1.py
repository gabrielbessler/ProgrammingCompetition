'''
You have been given an integer  which represents the length of one of cathetus of a right-angle triangle.
You need to find the lengths of the remaining sides. There may be multiple possible answers; any one will be accepted.

'''
#!/bin/python3

import sys
import math

def pythagoreanTriple(a):

    if a % 2 == 1: #a is odd
        k = (a - 1) // 2
        b = 2*(k+1)*k
        c = (k+1)**2 + k**2
        return int(a), int(b), int(c)
    else: #a is even
        numDiv = 0
        while a % 2 != 1: 
            a //= 2
            numDiv += 1
        if a == 1: # this means a was a power of 2 
            a *= (2 ** numDiv)
            multiple = a // 4
            return int(a), int(3 * multiple), int(5 * multiple)
        else: 
            k = (a - 1) // 2
            b = 2*(k+1)*k
            c = (k+1)**2 + k**2
            mul = 2 ** numDiv
            return int(a * mul), int(b*mul), int(c*mul)

# for some reason integer division is required (floating point math is annoying) 

a = int(input().strip())
triple = pythagoreanTriple(a)
print (" ".join(map(str, triple)))