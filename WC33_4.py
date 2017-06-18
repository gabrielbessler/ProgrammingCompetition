#!/bin/python3

import sys
import time

def findLargestRect(t):
    # There are waaaay too many rectangles we can make (because the biggest area possible is 10**5)
    # Which means we could have 10**5 1-area rects + almost 10**5 2-area rect... until 10**5 area rects
    # Which totals 10**5 **2

    #Let's consider cases where there are no leading 0s (so it's just 1-9)

    #Say it's a palindrome of even length...
    #This means we have an EVEN number of each character

    #Say it's a palindrome of odd length...
    #e.g. 2233322
    #We then can have an ODD number of 1 character, and all other characters must be even.

    #Therefore, for digits 1-9, a palindrome can be made IFF
    #We can 0 or 1 characters with an ODD amount of digits,
    #Every other character occurs in an even amount

    #Now let's say it is allowed to cotain 0...
    #Something that is a palindrome from the previous rules...
    #Let's say it's an even number palindrome...
    #That just means we need a pair of one character that is not a zero
    #Our sequence already satisfies this, so an even palindrome (meeting previous requirements) is a
    #Palindrome as long as it contains a non-zero character

    #For odd numbers, if our zero is the one is even amount that's fine
    #We just need the 0 to not be the ONLY ONE in even amount

    #So now we have our rules for checking is something is a palindrome (computationally simple)

    #In addition, the rectangle with the largest area is the same thing as searching for the palindrome with the most digits

    maxHeight = len(t)
    maxWidth = len(t[0])

    for rectHeight in range(maxHeight, 0, -1):
        for rectWidth in range(maxWidth, 0, -1):
            possibleStartingX = maxWidth - rectWidth + 1
            possibleStartingY = maxHeight - rectHeight + 1
            for x in range(possibleStartingX):
                for y in range(possibleStartingY):
                    startingPos = (x,y)



def getRectNm():
    # First, we know that m,n have to be smaller than 10**5
    # also, we know that n*m <= 10**5
    L = []
    for m in range(1,10**5):
        n = int(10**5 / m)
        L.append(n*(n+1)*m*(m+1) /4 )
    print(max(L))

def testFunc():
    st = time.time()
    for i in range(1000000):
        for j in range(100):
            a = 1+1
    print(time.time() - st)

def isPalindrome(string):
    letterCount = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7':0 , '8':0 , '9': 0, '0': 0}
    for letter in string:
        letterCount[letter] += 1

    for num in range(10):
        if letterCount[num] % 2 == 0:
          pass
        else:
            pass

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
table = []
for table_i in range(n):
   table_t = [int(table_temp) for table_temp in input().strip().split(' ')]
   table.append(table_t)
print(findLargestRect(table))