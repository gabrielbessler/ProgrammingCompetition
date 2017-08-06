#!/bin/python3

import sys
import time
from math import log

'''
Problem Statement:

For a given integer n, there is a tower built from 3**n blocks stacked vertically.
Each of these blocks can be colored in 3 different colors: red, green or blue.
How many different colorings of the tower can be created? Two colorings are considered
different if and only if there exists at least one block with different colors in the colorings.
Since the result can be a huge number, apply a modulo 10**9 + 7 on the result.

My Solution:

If there are k blocks, and each block has 3 possible colors, then we have 3**k possible colorings.
We know that k = 3**n, s.t. the number of colorings C is

C = 3**3**n

'''

def towerColoring(num):
    '''

    '''
    total = 3
    while num > 1:
        total *= 3
        total %= (10**9 + 7)
        num -= 1
    new_total = 3
    while total > 1:
        new_total *= 3
        new_total %= (10**9 + 7)
        total -= 1
    return new_total

def towerColoring2(num):
    '''
    Naive approach to solving 3**3**n mod 10**9 + 7,
    by simply computing the value and then taking its modulo. 
    '''
    return (3 ** (3 ** num)) % (10**9 + 7)

def towerColoring3(num):
    '''
    This is the fast algorithm we use.
    '''
    step_one = int(findPower(3, num, 10**9 + 6))
    step_two = findPower(3, step_one, 10**9 + 7)
    return step_two

def findPower(base, exp, mod=0):
    '''
    Fast algorithm for finding 
    (base ** exp) % mod
    '''
    binary_power_rep = bin(exp)[2:]
    binary_digit_parts = []
    for i in range(len(binary_power_rep)):
        binary_digit_parts += [(2 ** (len(binary_power_rep) - 1 - i)) * int(binary_power_rep[i])]
    totals = []
    for power in binary_digit_parts:
        if power != 0:
            value = base
            for j in range(int(log(power,2))):
                value **= 2
                if mod != 0:
                    value %= (mod)
            totals.append(value)
    total = 1
    for i in totals:
        total *= i
        if mod != 0:
            total %= (mod)
    if mod == 0:
        return total
    else:
        return total % mod

n = int(input().strip())
result = towerColoring3(n)
print(result)

'''
Speed Comparison

test_num = 16

st = time.time()
print(towerColoring(test_num))
print("First Trial: " + str(time.time() - st))
print("============================")

st = time.time()
print(towerColoring2(test_num))
print("Second Trial: " + str(time.time() - st))
print("============================")

st = time.time()
print(towerColoring3(test_num))
print("Third Trial: " + str(time.time() - st))
print("============================")
'''
