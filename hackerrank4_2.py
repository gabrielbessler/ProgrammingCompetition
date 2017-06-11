import sys
from functools import reduce
import time

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
    ''' Gets all of the divisors of a given number '''
    divs = []
    for i in range(1, int(1 + num ** .5)):
        if num % i == 0:
            divs.append(i)
            div2 = num // i
            if i != div2:
                divs.append(div2)
    divs.sort()
    return divs

def gcd(a,b):
    ''' Finds the greatest common divisor of two integers. '''
    if a < b: # require a > b
        A = b
        b,a = a,A
    while b != 0:
        a, b = b, a % b
    return a

def totients(n):
    ''' Computes the totient function using the greatest common divisor function. '''
    if n == 1:
        return 1
    totients = 0
    for i in range(1, n):
        if gcd(n,i) == 1:
            totients += 1
    return totients

def makeDivisorTreeOld(roots, d): # d == depth
    if d == 0:
        return roots
    newRoots = []
    for i in roots:
        newRoots += getDivisors(i)
    return makeDivisorTree(newRoots, d - 1)

def makeDivisorTreeOld(roots, d): # d == depth
    st = time.time()
    newRoots = []
    divisors = {}
    while d > 0:
        for i in roots:
            if i not in divisors:
                divisors[i] = getDivisors(i)
            newRoots += divisors[i]
        roots = newRoots
        newRoots = []
        d -= 1
    print(time.time() - st)
    return sum(roots)

def makeDivisorTree(root, levels): # d == depth
    #Start the timer
    st = time.time()

    numbersCount = {}

    #First, we get all of the divisors of our starting num
    rootDivisors = getDivisors(root)

    #We make a dictionary entry for each divisor
    for i in rootDivisors:
        numbersCount[i] = 0

    #To begin, we only have 1 of the root and no other number
    numbersCount[root] = 1

    divisors = {}
    #While we still have levels to go
    while levels > 0:
        #We go through the divisors in order from smallest to largest
        for divisor in rootDivisors:
            #One doesn't affect anything
            if divisor == 1:
                pass
            else:
                #For each number, we get how many of
                #That number we currently have
                divisorCount = numbersCount[divisor]
                #Now we check if we already have its divisors
                if divisorCount != 0: 
                    if divisor not in divisors:
                        #if not, calculate them
                        divisors[divisor] = getDivisors(divisor)
                    for nums in divisors[divisor]:
                        if nums == divisor: 
                            pass
                        else: 
                            numbersCount[nums] += divisorCount
        
        levels -= 1

    total = 0
    for i in rootDivisors: 
        total += numbersCount[i] * i
    
    print(time.time() - st)
    return total

def sumTotientTree(n,d):
    divisorTree = makeDivisorTree([n], d)
    totientTree = []
    for i in divisorTree:
        totientTree += [totients(i)]
    return sum(totientTree)

def divisorExploration(m, a, d):
    #p[i] is the ith prime, which means we need m primes
    #we know that m has an upper bound of 1000,
    #so we just need the first 1000 primes
    #we do this with a sieve up to n = 10000
    p = [1] + getPrimes() # adding 1 makes sure the indices are correct
    L = [p[i]** (a + i) for i in range(1, m+1)]#should go from 1 to m
    n = reduce(lambda x, y: x*y, L)
    return makeDivisorTree(n, d-1) % (10**9 + 7)
    #return sumTotientTree(n,d) % (10**9 + 7)

q = int(input().strip())
for a0 in range(q):
    m, a, d = input().strip().split(' ')
    m, a, d = [int(m), int(a), int(d)]
    result = divisorExploration(m, a, d)
    print(result)