'''
There are n different candies in total.
Three kinds of people:

a of them want to get odd number of candies,
b of them want to get even number of candies,
c simply don't care about parity of candies they get.

Find the number of ways to divide all candies between everybody
(some people may not receive a candy).

Constraints

n <= 10**9
a,b,c <= 50000
1 <= a + b + c
'''
''' E.g.

3 candies, A, B, C
a = 1, b = 1, c = 0

Soln: 4 ways b/c
{A}{B,C}
{B}, {C,A}
{C}, {A,B}
{A,B,C} {}
'''

#!/bin/python3

import sys

def parity_party(n, a, b, c):
    return 0

n, a, b, c = input().strip().split(' ')
n, a, b, c = [int(n), int(a), int(b), int(c)]
result = parity_party(n, a, b, c)
print(result)
