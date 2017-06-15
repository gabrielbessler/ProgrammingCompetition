def findPalindrome(s): 
    stringLen = len(s) 
    L = [[0 for i in range(stringLen)] for j in range(stringLen)] 
    for i in range(stringLen):
        L[i][i] = 1
    for substring_length in range(2, stringLen+1): # (We already did the diagonals, length 1)
        for i in range(stringLen - substring_length + 1): 
            j = i + substring_length - 1
            startingLetter = s[i] 
            endingLetter = s[j]
            if substring_length == 2 and startingLetter == endingLetter: 
                L[i][j] = 2 
            elif startingLetter == endingLetter:
                L[i][j] = 2 + L[i+1][j-1] #We move down a row and left a column 
            else: 
                L[i][j] = max(L[i+1][j], L[i][j-1])
    return L[0][-1]
