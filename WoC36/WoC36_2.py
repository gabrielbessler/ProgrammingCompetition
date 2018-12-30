#!/bin/python3

import sys

def revisedRussianRoulette(doors):
   
    unlock_count = 0
    num_locked = sum(doors)
    
    for index, door_status in enumerate(doors): 
        if door_status == 1: 
            unlock_count += 1
            door_status = 0
            if index < len(doors) - 1:
                doors[index + 1] = 0
                    
    return [unlock_count, num_locked]
        
if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print (" ".join(map(str, result)))
