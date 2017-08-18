import sys
from functools import reduce, lru_cache

# Initially, the approach was to make a tree of all
# of the divisors. 

# Note that the recursive summing is the same as just
# Summing the very last row once. 

# Additionally, note that for any given number, the sum
# of the totient of the divisors is the same as the 
# number itself. 

def get_primes(upper_bound=10000):
    ''' Uses a sieve to get all prime numbers up to upperBound '''
    possiblePrimes = [2] + list(range(3, upper_bound, 2))
    for i in range(3, 1000):
        if i in possiblePrimes:
            possiblePrimes = list(filter(lambda x: x % i != 0 or x == i, possiblePrimes))
    return possiblePrimes

@lru_cache(None)
def make_div_tree(prime, power, depth):
    if power == 1:
        return prime + depth
    elif depth == 0:
        return (prime ** power)
    return make_div_tree(prime, power-1, depth) + make_div_tree(prime, power, depth - 1)

def divisor_exploration(m, a, d):
    p = [1] + get_primes()
    return (reduce(lambda w, z: (w * z) % (10**9 + 7), [make_div_tree(p[i], (a+i), d - 1) for i in range(1, m+1)])) % (10**9 + 7), time() - s

sys.setrecursionlimit(3000)
q = int(input().strip())
for a0 in range(q):
    m, a, d = input().strip().split(' ')
    m, a, d = [int(m), int(a), int(d)]
    result = divisor_exploration(m, a, d)
    print(result)