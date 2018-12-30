#!/bin/python3

import sys
from functools import reduce

'''
Given Jack's current ticket number, find and print the next lucky ticket number

A lucky ticket is a six-digit number on the ticket in which sum of the first three
digits is equal to the sum of the last three digits (in this case, we are only dealing
with six digit numbers).
'''

def next_lucky_number(curr_val):
    while True:
        curr_val_str = str(starting_val)
        if reduce(lambda x, y: int(x) + int(y), curr_val_str[:3]) == reduce(lambda x, y: int(x) + int(y), curr_val_str[3:]):
            return curr_val
        curr_val += 1

if __name__ == "__main__":
    starting_val = int(input().strip())
    result = next_lucky_number(starting_val+1)
    print(result)
