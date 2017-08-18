#!/bin/python3

import sys
import time

# pylint: disable=C0103

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

#In addition, the rectangle with the largest area is the same thing as 
# searching for the palindrome with the most digits

def find_largest_rect(t):
    '''

    '''
    maxHeight = len(t)
    maxWidth = len(t[0])

    ans = []
    largestAreaFound = 0
    for rectHeight in range(maxHeight, 0, -1):
        for rectWidth in range(maxWidth, 0, -1):
            if rectHeight * rectWidth < largestAreaFound:
                break
            foundAns = False
            for x in range(maxWidth - rectWidth + 1):
                for y in range(maxHeight - rectHeight + 1):
                    startingPos = (x, y)
                    nums = []
                    for row in range(y, y+rectHeight):
                        nums.extend(t[row][x:x+rectWidth])
                    if is_palindrome(nums):
                        foundAns = True
                        largestAreaFound = rectHeight * rectWidth
                        ans.append([largestAreaFound, startingPos, rectWidth, rectHeight])
                        break
                if foundAns:
                    break
    maxv = 0
    maxv_i = 0
    for i in range(len(ans)):
        if ans[i][0] > maxv:
            maxv = ans[i][0]
            maxv_i = i
    print(str(ans[maxv_i][0]) + '\n' + str(ans[maxv_i][1][0]) +" "+ str(ans[maxv_i][1][1]) + " " + str(ans[maxv_i][1][1] + ans[maxv_i][3] - 1) + " " + str(ans[maxv_i][1][0] + ans[maxv_i][2] - 1))

def is_palindrome(string):
    '''
        Counts the number of numbers in a string. 
        Then sees if the number of numbers makes it 
        possible for the string to be a palindrome. 
    '''
    if len(string) == 1:
        return True
    else:
        letterCount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0, 8:0, 9: 0, 0: 0}
        for letter in string:
            letterCount[letter] += 1

        foundOdd = 0
        nonZeroPair = False
        for num in range(10):
            if letterCount[num] % 2 == 0:
                if num != 0:
                    nonZeroPair = True
            else:
                if num != 0 and letterCount[num] > 1:
                    nonZeroPair = True
                foundOdd += 1
        if foundOdd > 1:
            return False
        else:
            return nonZeroPair

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
table = []
for table_i in range(n):
   table_t = [int(table_temp) for table_temp in input().strip().split(' ')]
   table.append(table_t)
st = time.time()
print(find_largest_rect(table))
print(time.time() - st)
