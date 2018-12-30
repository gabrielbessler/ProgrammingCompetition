#!/bin/python3

import os
import sys

#
# Complete the maximumProgramValue function below.
#
def maximumProgramValue(n):
    max_val = 0
    # First, read all of the instructions
    for i in range(n): 
        in_text = input()
        instruction = in_text[:3]
        num = int(in_text[4:])
        if instruction == "set": 
            # We only want to set if the number we create is larger
            if num > max_val: 
                max_val = num
        elif instruction == "add":
            # We never want to add a negative number
            if num > 0: 
                max_val += num 
                
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = maximumProgramValue(n)

    fptr.write(str(result) + '\n')

    fptr.close()
