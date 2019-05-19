# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem B. Pottery Lottery
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/00000000001461c8
#
# Time:  O(1)
# Space: O(1)
#

import sys
import heapq

def pottery_lottery():
    D = P-1

    # day 1 ~ N
    for i in xrange(N):  # sabotage
        _ = input()
        D -= 1
        print (i % S)+1, 1
        sys.stdout.flush()

    # day N+1 ~ N+V
    heap = []
    for i in xrange(V):  # inspect
        _ = input()
        D -= 1
        print i+1, 0
        sys.stdout.flush()
        heapq.heappush(heap, (len(raw_input().strip().split()), -i))
    
    # day N+V+1 ~ P-1
    _, candidate = heapq.heappop(heap)
    while D:  # sabotage
        _ = input()
        D -= 1
        count, i = heapq.heappop(heap)
        print -i+1, 1
        sys.stdout.flush()
        heapq.heappush(heap, (count+1, i))
 
    # day P
    _ = input()
    print -candidate+1, P
    sys.stdout.flush()

P, V = 100, 20
N, S = 60, 14  # tuned by testing_tool.py (243/250)
assert(N + S < P)
for case in xrange(input()):
    pottery_lottery()
