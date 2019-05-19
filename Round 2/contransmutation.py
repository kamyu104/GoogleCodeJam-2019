# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem D. Contransmutation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146185
#
# Time:  O(M)
# Space: O(M)
#

from collections import deque

def contransmutation():
    M = input()
    R = []
    for _ in xrange(M):
        R.append(map(lambda x: int(x)-1, raw_input().strip().split()))
    G = map(int, raw_input().strip().split())

    # check if canMakeLead
    parents = [[] for i in xrange(M)]
    for parent in xrange(M):
        for child in R[parent]:
            parents[child].append(parent)
    canMakeLead = [False]*M
    canMakeLead[0] = True
    q = deque([0])
    while q:
        i = q.popleft()
        for j in parents[i]:
            if not canMakeLead[j]:
                canMakeLead[j] = True
                q.append(j)

    # check if isReachable
    MakeLead = [[child for child in children if canMakeLead[child]] for children in R]
    isReachable = [False]*M
    q = deque()
    for i in xrange(M):
        if G[i] > 0:
            isReachable[i] = True
            q.append(i)
    while q:
        i = q.popleft()
        for j in MakeLead[i]:
            if not isReachable[j]:
                isReachable[j] = True
                q.append(j)
    for i in xrange(M):
        if not isReachable[i]:
            MakeLead[i] = []
    if not isReachable[0]:
        return 0

    # check if any trouble
    if MakeLead[0]:
        curr = 0
        if len(MakeLead[curr]) > 1:
            return "UNBOUNDED"
        curr = MakeLead[curr][0]
        while curr != 0:
            if len(MakeLead[curr]) > 1:
                return "UNBOUNDED"
            curr = MakeLead[curr][0]
        MakeLead[curr] = []

    # Kahn's algorithm
    total = list(G)
    numParents = [0 for i in xrange(M)]
    for parent in xrange(M):
        for j in MakeLead[parent]:
            numParents[j] += 1
    q = deque([i for i in xrange(M) if numParents[i] == 0])
    while q:
        i = q.popleft()
        for j in MakeLead[i]:
            total[j] += total[i]
            numParents[j] -= 1
            if numParents[j] == 0:
                q.append(j)
    return "UNBOUNDED" if any(numParents) else total[0] % MOD

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, contransmutation())
