import sys
from functools import reduce, lru_cache
from time import time 

def getPrimes(upperBound = 9000):
    possiblePrimes = [2] + list(range(3,upperBound,2))
    for i in range(3,1000):
        if i in possiblePrimes:
            possiblePrimes = list(filter(lambda x: x % i != 0 or x == i, possiblePrimes))
    return possiblePrimes

@lru_cache(None)
def makeDivTree(prime, power, depth):
    if power == 1: 
        return prime + depth
    elif depth == 0: 
        return (prime ** power) % (10**9 + 7)
    return makeDivTree(prime, power-1, depth) + makeDivTree(prime, power, depth - 1)

def divisorExploration(m, a, d):
    p = [1] + getPrimes() 
    s = time() 
    return (reduce(lambda w, z: (w * z) % (10**9 + 7), [makeDivTree(p[i], (a+i), d - 1) for i in range(1, m+1)])) % (10**9 + 7), time() - s

sys.setrecursionlimit(3000)
q = int(input().strip())
for a0 in range(q):
    m, a, d = input().strip().split(' ')
    m, a, d = [int(m), int(a), int(d)]
    result = divisorExploration(m, a, d)
    print(result)