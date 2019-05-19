# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem B. Pottery Lottery
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/00000000001461c8
#
# Time:  O(PlogV)
# Space: O(V)
#

from sys import stdout
from heapq import heappush, heappop

def put(i, v, D):
    _ = input()
    D[0] -= 1
    print i+1, v
    stdout.flush()

def pottery_lottery():
    D = [P]

    # day 1 ~ N1
    for i in xrange(N1):  # sabotage
        put(i%S, 1, D)

    # day N1+1 ~ N1+V
    min_heap = []
    for i in xrange(V):  # inspect
        put(i, 0, D)
        heappush(min_heap, (len(raw_input().strip().split()), -i))
    
    # day N1+V+1 ~ N1+V+N2
    candidates = []
    for _ in xrange(C):
        candidates.append(-heappop(min_heap)[1])
    for _ in xrange(N2):  # sabotage
        count, i = heappop(min_heap)
        put(-i, 1, D)
        heappush(min_heap, (count+1, i))

    # day N1+V+N2+1 ~ N1+V+N2+C
    min_heap = []
    for i in candidates:  # inspect
        put(i, 0, D)
        heappush(min_heap, (len(raw_input().strip().split()), i))

    # day N1+V+N2+C+1 ~ P-1
    candidate = -heappop(min_heap)[1]
    while D[0] > 1:  # sabotage
        count, i = heappop(min_heap)
        put(-i, 1, D)
        heappush(min_heap, (count+1, i))
 
    # day P
    put(candidate, P, D)

P, V = 100, 20
N1, S, N2, C = 60, 14, 14, 2  # tuned by testing_tool.py (247/250)
assert(N1 + V + N2 + C < P)
for case in xrange(input()):
    pottery_lottery()
