from utils import * 

def getFuel(massL):
    L = [(mass // 3) - 2 for mass in massL]
    return sum(L)

def getTotalFuel(massL): 
    L = [(mass // 3) - 2 for mass in massL]
    for i in range(len(L)): 
        totalFuel = L[i]
        difference = totalFuel
        while True: 
            difference = (difference // 3) - 2
            if difference <= 0: 
                L[i] = totalFuel
                break
            totalFuel += difference
    return sum(L)

def main(): 
    return getTotalFuel(fileToIntList('test.txt'))