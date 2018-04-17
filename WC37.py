#!/bin/python3

import os
import sys

# Complete the averageOfTopEmployees function below.
def averageOfTopEmployees(rating):
    print("{:,.2f}".format((lambda x:(round(0.0000001+100*(sum(x)/len(x))))/100)(list(filter(lambda l:l>=90,rating))))) 
    
if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    averageOfTopEmployees(rating)
