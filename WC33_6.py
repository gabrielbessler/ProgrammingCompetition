#!/bin/python3

import sys
from collections import defaultdict
from time import time
from random import randint
from functools import lru_cache

def BFS(adjecency_list, start_node, end_node):
    parent_dict = {start_node: None}
    curr = [start_node]
    found_end = False
    while curr:
        next = []
        for vertex in curr:
            for next_v in adjecency_list[vertex]:
                if next_v not in parent_dict:
                    parent_dict[next_v] = vertex
                    if next_v == end_node:
                        found_end = True
                        break
                    next.append(next_v)
            if found_end:
                break
        if found_end:
            break
        curr = next
    path = []
    curr_node = end_node
    while curr_node is not None:
        path.append(curr_node)
        curr_node = parent_dict[curr_node]
    return path[::-1]

def depth_first_search(adjecency_list, start_node):
    visited_nodes = set()
    stack = [start_node]
    while stack:
        #We remove the last item from the stack,
        #and store it as the vertex we're currently looking at
        vertex = stack.pop()
        if vertex not in visited_nodes:
            visited_nodes.add(vertex)
            stack.extend(adjecency_list[vertex] - visited_nodes)
    return visited_nodes

@lru_cache(None)
def getAns(u, v):
    path = BFS(adjecency_list, u, v)
    new_s = ""
    for node_num in path:
        new_s += s[node_num - 1]
    count_occur = 0
    for i in range(len(new_s) - len(p) + 1):
        if new_s[i:i+len(p)] == p:
            count_occur += 1
    return count_occur

adjecency_list = defaultdict(set)
n, q = input().strip().split(' ')
n, q = [int(n), int(q)]
s = input().strip()
p = input().strip()
for a0 in range(n-1):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    adjecency_list[u].add(v)
    adjecency_list[v].add(u)

total_time = 0
for i in range(1000000):
    u, v = [randint(1, 5), randint(1, 5)]
    st = time()
    getAns(u, v)
    total_time += time() - st
print(total_time)

'''
for a0 in range(q):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    print(getAns(u,v))
'''
