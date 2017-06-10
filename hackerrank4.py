#!/bin/python3

import sys

def getPrimes():
    ''' Inefficient prime algorithm I had already made '''
    upperBound = 10000

    #Our possible primes are odds from 3 to 200,000
    possiblePrimes = [2] + list(range(3,upperBound,2))

    #Go through all of the possible factors of any of those numbers (3 to 447)
    for i in range(3,1000):
        if i in possiblePrimes:
            #could also do this by looping through all of the multiples of i...probably better
            possiblePrimes = list(filter(lambda x: x % i != 0 or x == i, possiblePrimes))
    return possiblePrimes

def getDivisors(num):
    #TODO: make it output the divisors in order
    ''' Gets all of the divisors of a given number '''
    divs = [1]
    for i in range(2, int(1 + num ** .5)):
        if num % i == 0:
            divs.append(i)
            div2 = num // i
            if i != div2:
                divs.append(div2)
    return divs

def divisorExploration(m, a, d):
    ''' '''
    #p[i] is the ith prime, which means we need m primes
    #we know that m has an upper bound of 1000,
    #so we just need the first 1000 primes
    #we do this with a sieve up to n = 10000
    p = [1] + getPrimes() #adding 1 makes sure the indices are correct
    L = [p[i]** a + i for i in range(1, m+1)]#should go from 1 to m
    n = reduce(lambda x, y: x*y, L)

    currTree = [n]
    while d > 1:
        for i in range(len(currTree)):
            currTree[i] =
        divisors = getDivisors(n)
        d -= 1

q = int(input().strip())
for a0 in range(q):
    m, a, d = input().strip().split(' ')
    m, a, d = [int(m), int(a), int(d)]
    result = divisorExploration(m, a, d)
    print(result)
