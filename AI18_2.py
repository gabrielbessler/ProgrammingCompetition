#!/bin/python3

import sys
import time
from math import log

def towerColoring(n):
    total = 3
    while n > 1:
        total *= 3
        total %= (10**9 + 7)
        n -= 1
    newTotal = 3
    while total > 1:
        newTotal *= 3
        newTotal %= (10**9 + 7)
        total -= 1
    return newTotal

def towerColoring2(n):
    return (3 ** (3 ** n)) % (10**9 + 7)

def findPower(base, exp, mod = 0):
    binaryPowerRep = bin(exp)[2:]
    binaryDigitParts = []
    for i in range(len(binaryPowerRep)):
        binaryDigitParts += [(2 ** (len(binaryPowerRep) - 1 - i)) * int(binaryPowerRep[i])]
    totals = []
    for power in binaryDigitParts:
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

def towerColoring3(n):
    stepOne = int(findPower(3, n, 10**9 + 6))
    stepTwo = findPower(3, stepOne, 10**9 + 7)
    return stepTwo

#n = int(input().strip())
#result = towerColoring(n)
#print(result)

'''
testNum = 16

st = time.time()
print(towerColoring(testNum))
print("First Trial: " + str(time.time() - st))
print("============================")

st = time.time()
print(towerColoring2(testNum))
print("Second Trial: " + str(time.time() - st))
print("============================")

st = time.time()
print(towerColoring3(testNum))
print("Third Trial: " + str(time.time() - st))
print("============================")
'''