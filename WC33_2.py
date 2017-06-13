#!/bin/python3

import sys

def patternCount(s):
    patternNum = 0 
    inPattern = False 
    for i in range(len(s)):
        currLetter = s[i] #figure out what the curr num is 
        if i == len(s) - 1: 
            #if we are at the last letter, we can only be ending a pattern 
            if inPattern == True and currLetter == '1': 
                patternNum += 1
                
        else: 
            nextLetter = s[i+1]
            if currLetter == '1': 
                if nextLetter == '0': 
                    #If the current letter is a one and then next letter is a zero, then we are starting a pattern
                    inPattern = True
                else: 
                    continue
            elif currLetter == '0': 
                if nextLetter == '1': 
                    #if the current letter is a zero and then next letter is a one, then we are ending a pattern (if we are in one)
                    if inPattern == True: 
                        patternNum += 1
                        inPattern = False 
                elif nextLetter == '0': 
                    # if the current letter is a zero and the next letter is also a zero, the pattern simply continues so nothing changes
                    continue
            else: 
                # if we see anything that isnt a 0 or a 1, we must be breaking a pattern
                inPattern = False 
    return patternNum

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)
