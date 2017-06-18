#!/bin/python3

import sys

# A string s contains many patterns of the form 1(0+)1,
# where (0+) represents any non-empty consecutive sequence of 0's.
# The patterns are allowed to overlap.

def patternCount(s):
    ''' Count the number of times the patter 1(0+)1 occurs in a string. '''
    pattern_num = 0
    in_pattern = False
    for i, curr_letter in enumerate(s):
        #figure out what the current number is
        if i == len(s) - 1:
            #if we are at the last letter, we can only be ending a pattern
            if curr_letter == '1' and in_pattern:
                pattern_num += 1
        else:
            next_letter = s[i+1]
            if curr_letter == '1':
                if next_letter == '0':
                    #If the current letter is a one and then next letter is a zero,
                    #then we are starting a pattern
                    in_pattern = True
                else:
                    continue
            elif curr_letter == '0':
                if next_letter == '1':
                    #if the current letter is a zero and then next letter is a one,
                    #then we are ending a pattern (if we are in one)
                    if in_pattern:
                        pattern_num += 1
                        in_pattern = False
                elif next_letter == '0':
                    #if the current letter is a zero and the next letter is also a zero,
                    #the pattern simply continues so nothing changes
                    continue
            else:
                # if we see anything that isnt a 0 or a 1, we must be breaking a pattern
                in_pattern = False
    return pattern_num

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
