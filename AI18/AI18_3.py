#!/bin/python3

import sys
from functools import reduce

'''
Problem Statement

We're considering infinite sums (from n=1 to n=inf), of the form
    P(n) / Q(n),                    Q(n) != 0
We know that if deg P <= deq Q - 2, the series converges (although
the sum can be irrational). Therefore, we consider a special case of

Q(x) = (x + a_1)(x + a_2)...(x + a_n)
P(x) = b_0 + b_1*x + ... + b_n-2*x**(n-2),

with the constraints that all a_i are distinct positive integers.

Constraints

2 <= n <= 5000
0 <= a_i <= 5000
0 <= b_i <= 10**9

Output Format

If the answer is an irreducible fraction a/b, print a*b**-1 mod (10**9 + 7), where b**-1 is multiplicative
inverse of b modulo 10**9 + 7. It is guaranteed that b mod 10**9 + 7 != 0.

'''

def rational_sums(n, a, b):
    '''
    This performs a partial fraction decomposition of a given fraction.
    '''
    # First we want to find each numerator for partial fractions...

    #This first takes our x value, then adds up each term in the numerator after plugging in x
    top = lambda x: sum(map(lambda i: b[i] * (x ** i), range(len(b))))
    bot = lambda x: reduce(lambda j, k: j if k == 0 else k if j == 0 else j*k,
                           map(lambda i: x + a[i], range(len(a))))

    #We need as many numerators as there are denominators (for partial fractions), so
    numerators = [top(-1*a[i])/bot(-1*a[i]) for i in range(n)]
    terms = lambda x: [numerators[i]/(x + a[i]) for i in range(n)]

    repetitions = 100000

    total = 0
    for l in range(1, repetitions):
        total += sum(terms(l))

    return int(round(total % (10**9 + 7)))

n = int(input().strip())                            #The degree of the function
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
result = rational_sums(n, a, b)
print(result)
