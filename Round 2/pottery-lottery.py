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

def pottery_lottery():
    D = P-1

    # day 1 ~ N1
    for i in xrange(N1):  # sabotage
        _ = input()
        D -= 1
        print (i % S)+1, 1
        stdout.flush()

    # day N1+1 ~ N1+V
    min_heap = []
    for i in xrange(V):  # inspect
        _ = input()
        D -= 1
        print i+1, 0
        stdout.flush()
        heappush(min_heap, (len(raw_input().strip().split()), -i))
    
    # day N1+V+1 ~ N1+V+N2
    candidates = []
    for _ in xrange(C):
        candidates.append(heappop(min_heap)[1])
    for _ in xrange(N2):  # sabotage
        _ = input()
        D -= 1
        count, i = heappop(min_heap)
        print -i+1, 1
        stdout.flush()
        heappush(min_heap, (count+1, i))

    # day N1+V+N2+1 ~ N1+V+N2+C
    min_heap = []
    for i in candidates:  # inspect
        _ = input()
        D -= 1
        print -i+1, 0
        stdout.flush()
        heappush(min_heap, (len(raw_input().strip().split()), i))

    # day N1+V+N2+C+1 ~ P-1
    candidate = heappop(min_heap)[1]
    while D:  # sabotage
        _ = input()
        D -= 1
        count, i = heappop(min_heap)
        print -i+1, 1
        stdout.flush()
        heappush(min_heap, (count+1, i))
 
    # day P
    _ = input()
    print -candidate+1, P
    stdout.flush()

P, V = 100, 20
N1, S, N2, C = 60, 14, 14, 2  # tuned by testing_tool.py (247/250)
assert(N1 + V + N2 + C < P)
for case in xrange(input()):
    pottery_lottery()
