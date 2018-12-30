import sys
from functools import reduce, lru_cache

'''
Problem Statement for Divisor Exploration 3

We have q queries of (m, a, d), s.t.

    n_i = p_i**(a + i), where p_i is the i'th prime.

and n is the product of all n_i from i=1 to i=m.
Using n along with d, create a tree T such that
    n is the root node
    all the children of a node are its divisors (including 1 and itself)
    continue expanding until T has depth d
Now, replace the leaves (nodes at maximum depth) such that each leaf
is its own totient function. Next, its parent are equal to the sum of the
values of its children.
Do this iteratively until you reach the root node of the tree, and output its
value mod (10**9 + 7)

Constraints

q <= 50
m <= 1000
a <= 1000
d <= 1000
'''

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
        return prime ** power
    return make_div_tree(prime, power-1, depth) + make_div_tree(prime, power, depth - 1)

def divisor_exploration(m, a, d):
    p = [1] + get_primes()
    return (reduce(lambda w, z: (w * z) % (10**9 + 7), \
        [make_div_tree(p[i], (a+i), d - 1) for i in range(1, m+1)])) % (10**9 + 7), time() - s

sys.setrecursionlimit(3000)
q = int(input().strip())
for a0 in range(q):
    m, a, d = input().strip().split(' ')
    m, a, d = [int(m), int(a), int(d)]
    result = divisor_exploration(m, a, d)
    print(result)
