#!/bin/python3

import sys
from functools import reduce 

def onceInATram(x):
    # Complete this function
    while True:
        x_str = str(x) 
        if reduce(lambda x,y: int(x) + int(y), x_str[:3]) == reduce(lambda x,y: int(x) + int(y), x_str[3:]):
            return x
        x+=1

if __name__ == "__main__":
    x = int(input().strip())
    result = onceInATram(x+1)
    print(result)
