#!/bin/python3

import sys
from functools import reduce

def rationalSums(n, a, b):
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
result = rationalSums(n, a, b)
print(result)
