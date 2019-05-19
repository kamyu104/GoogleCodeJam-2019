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

    # check if can_make_lead
    parents = [[] for _ in xrange(M)]
    for i in xrange(M):
        for child in R[i]:
            parents[child].append(i)
    can_make_lead = [False]*M
    can_make_lead[0] = True
    q = deque([0])
    while q:
        i = q.popleft()
        for j in parents[i]:
            if not can_make_lead[j]:
                can_make_lead[j] = True
                q.append(j)

    # check if is_reachable
    R_reach_lead = [[] for _ in R]
    is_reachable = [False]*M
    q = deque()
    for i in xrange(M):
        if not G[i]:
            continue
        is_reachable[i] = True
        R_reach_lead[i] = [child for child in R[i] if can_make_lead[child]]
        q.append(i)
    while q:
        i = q.popleft()
        for j in R_reach_lead[i]:
            if is_reachable[j]:
                continue
            is_reachable[j] = True
            R_reach_lead[j] = [child for child in R[j] if can_make_lead[child]]
            q.append(j)
    if not is_reachable[0]:
        return 0

    # check if bounded
    if R_reach_lead[0]:
        curr = 0
        if len(R_reach_lead[curr]) > 1:
            return "UNBOUNDED"
        curr = R_reach_lead[curr][0]
        while curr != 0:
            if len(R_reach_lead[curr]) > 1:
                return "UNBOUNDED"
            curr = R_reach_lead[curr][0]
        R_reach_lead[curr] = []

    # Kahn's algorithm
    indegrees = [0 for i in xrange(M)]
    for i in xrange(M):
        for j in R_reach_lead[i]:
            indegrees[j] += 1
    q = deque([i for i in xrange(M) if indegrees[i] == 0])
    while q:
        i = q.popleft()
        for j in R_reach_lead[i]:
            G[j] += G[i]
            indegrees[j] -= 1
            if indegrees[j] == 0:
                q.append(j)
    return "UNBOUNDED" if any(indegrees) else G[0] % MOD

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, contransmutation())
