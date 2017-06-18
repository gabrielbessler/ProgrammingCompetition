#!/bin/python3

import sys
import random
import time
from collections import defaultdict

# we have n letters in our alphabet - up to 100,000
# m is the # of integers we have - up to 1000
# a are the starting numbers
# k are how many different transformations we have - up to 1,000,000

def findPalindrome(s):
    '''
    
    '''
    # Given a string, we want to find the longest palindrome subsequence

    # We can do it using use-it-or-lose-it in recursion, but due to the repeating-subproblems,
    # Our alg will have a time complexity of O(2**n)

    # In order to get around this, we use dynamic programming
    # We start with the outside characters
    # If they are the same, we definitely want to use the, so we add 2 to our length and continue
    # The algorithm with the new sequence
    # If they are different, we solve the problem once ignoring the last character, and once using the first character
    # We basically solve the problem bottom-up instead of top-down in dynamic programming!

    # Cases:
    # If s is one character, then max length palindrome is 1
    # If s is two characters, max length palindrome is 2

    string_len = len(s)

    L = [[0 for i in range(string_len)] for j in range(string_len)]

    #If our string is n characters, we first make an nxn grid

    for i in range(string_len):
        L[i][i] = 1

    # The table should be symmetrical
    for substring_length in range(2, string_len+1): # (We already did the diagonals, length 1)
        # i is our row, j is our column (note that top-left is 0,0)
        for i in range(string_len - substring_length + 1):
            j = i + substring_length - 1
            startingLetter = s[i]
            endingLetter = s[j]
            # First, we have the special case of length 2
            if substring_length == 2 and startingLetter == endingLetter:
                L[i][j] = 2
            elif startingLetter == endingLetter:
                L[i][j] = 2 + L[i+1][j-1] #We move down a row and left a column
            else:
                L[i][j] = max(L[i+1][j], L[i][j-1])

    # The top right entry in our table is the answer for the entire word, so
    return L[0][-1]

def findLongestSubsequence(a, transfs, n):
    '''

    '''
    adjecency_list = defaultdict(set)
    for first_val, second_val in transfs:
        adjecency_list[first_val].add(second_val)
        adjecency_list[second_val].add(first_val)

    nodes = set([x for x in range(1, n+1)]) # creates all nodes
    groups = []
    while nodes:
        currNode = nodes.pop()
        group = depth_first_search(adjecency_list, currNode)
        groups.append(group)
        nodes -= set(group)

    # First we do all of the replacements to the list a
    for i in range(len(a)):
        for group in groups:
            if a[i] in group:
                a[i] = min(group)

    return findPalindrome(a)

def depth_first_search(adjecency_list, start_node):
    '''

    '''
    visited_nodes = set()
    stack = [start_node]
    while stack:
        # We remove the last item from the stack and store it as the vertex we're currently looking at
        vertex = stack.pop() 
        if vertex not in visited_nodes:
            visited_nodes.add(vertex)
            stack.extend(adjecency_list[vertex] - visited_nodes)
    return visited_nodes

test = False
if test == True:
    #Worst Case:
    #100000 letters in our alphabet
    numLetters = 100000
    numTranfs = 1000000

    #1000 integers in our starting string
    a = [random.randint(1, numLetters) for i in range(1000)]
    #1000000 transformations
    tranfs = [(random.randint(1, numLetters), random.randint(1, numLetters)) for i in range(numTranfs)]
    print('running....')
    ST = time.time()
    findLongestSubsequence(a, tranfs, numLetters)
    print(time.time() - ST)
else:
    n,k,m = input().strip().split(' ')
    n,k,m = [int(n),int(k),int(m)]
    transfs = []
    for a0 in range(k):
        x,y = input().strip().split(' ')
        x,y = [int(x),int(y)]
        transfs.append((x,y))
    a = list(map(int, input().strip().split(' ')))
    print(findLongestSubsequence(a, transfs, n))