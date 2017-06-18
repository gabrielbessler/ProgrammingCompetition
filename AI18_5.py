# We begin with the linear diophantine equation ax + by = c 
# we know this equation only has solutions if 
# c is a multiple of gcd(a, b). 
# This means that c can take on integer values 
# n * gcd(a, b) for any given a, b
# In addition, we know 
# if (x, y) is a solution, then the other solutions have the form (x + kv, y − ku)
# where k is an arbitrary const, s.t. 

# if (x,y) soln, all other solutions are of form (x + k*a/gcd(a,b), x + k*b/gcd(a,b))
#Therefore, 

# We let w = gcd(a,b) euclidian alg

# (1) (x^2 + y^2) must be a multiple of w
# (2) Once we find solution (x, y),  all other solutions are of form (x + k*a/w, x + k*b/w)

#!/bin/python3

import sys
import time
from functools import lru_cache

def gcd(a,b):
    ''' Finds the greatest common divisor of two integers. '''
    if a < b: # require a > b
        A = b
        b,a = a,A
    while b != 0:
        a, b = b, a % b
    return a


#(ax + by) must have gcd(a,b) as a factor 

def countSolutions(a, b, c, d):
    # Complete this function
    g = gcd(a, b)
    numSol = 0
    for x in range(1, c+1):
        for y in range(1, d+1): 
            if (x*x + a*x) % g == 0 and (y*y + b*y) % g == 0:
                if x*x + y*y == a*x + b*y:
                    numSol += 1
    return numSol
    
    
st = time.time()
tot = 0
for i in range(12, 20): 
    a = (countSolutions(100 * i, 100 * i, 100 * i, 100 * i))
    tot += a
print(time.time() - st, tot)

#q = int(input().strip())
#for a0 in range(q):
#    a, b, c, d = input().strip().split(' ')
#    a, b, c, d = [int(a), int(b), int(c), int(d)]
#    result = countSolutions(a, b, c, d)
#    print(result)