#!/bin/python3

import sys
import time

# pylint: disable=C0103

def findLargestRect(t):
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
                    if isPalindrome(nums):
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

def isPalindrome(string):
    if len(string) == 1:
        return True
    else:
        letterCount = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0 , 8:0 , 9: 0, 0: 0}
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
print(findLargestRect(table))
print(time.time() - st)