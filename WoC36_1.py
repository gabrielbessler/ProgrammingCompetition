#!/bin/python3

import sys

def acidNaming(acid_name):
    if len(acid_name) >= 5: 
        if acid_name[:5] == "hydro" and acid_name[-2:] == "ic":
            return "non-metal acid"
    
    if acid_name[-2:] == "ic":
        return "polyatomic acid"
    return "not an acid"
    
if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        acid_name = input().strip()
        result = acidNaming(acid_name)
        print(result)
