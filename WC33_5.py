#!/bin/python3
import sys
import random
import time
from collections import defaultdict

sys.setrecursionlimit(2000)
def search(curr_node, goal_node, visited):
    nextVisited = visited.copy()
    nextVisited.add(curr_node)
    if curr_node == goal_node:
        if goal_node == v:
            return 1
        elif goal_node == w:
            goal_node = v
    if adjecency_list[curr_node] - nextVisited == set():
        return 0
    else:
        waysToGo = adjecency_list[curr_node] - nextVisited
        total = 0
        for next_node in waysToGo:
            if search(next_node, goal_node, nextVisited) == 1:
                return 1
        return 0

def depth_first_search(adjecency_list, start_node, mid_node, end_node):
    visited_nodes = set()
    stack = [start_node]
    while stack:
        vertex = stack.pop() # We remove the last item from the stack and store it as the vertex we're currently looking at
        if vertex not in visited_nodes:
            visited_nodes.add(vertex)
            stack.extend(adjecency_list[vertex] - visited_nodes)
    return visited_nodes
'''
n, m, q = input().strip().split(' ')
n, m, q = [int(n), int(m), int(q)]
adjecency_list = defaultdict(set)


for a0 in range(m):
    u, v = input().strip().split(' ')
    u, v = [int(u), int(v)]
    adjecency_list[u].add(v)
    adjecency_list[v].add(u)
for a0 in range(q):
    u, v, w = input().strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]
    st = time.time()
    if (search(u, w, set())) == 1:
        print("YES")
    else:
        print("NO")
    print(st - time.time())
'''

adjecency_list = defaultdict(set)
st = time.time()
for a in range(20):
    for m in range(100):
        u,v = [random.randint(1,100), random.randint(1,100)]
        adjecency_list[u].add(v)
        adjecency_list[v].add(u)
    u, v, w = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
    print(u,v,w)

    if (search(u, w, set())) == 1:
        print("YES")
    else:
        print("NO")
print(time.time() - st)
