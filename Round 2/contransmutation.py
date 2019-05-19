# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem D. Contransmutation
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146185
#
# Time:  O(M)
# Space: O(M)
#

from collections import deque, defaultdict

def contransmutation():
    M = input()
    R = []
    for _ in xrange(M):
        R.append(map(lambda x: int(x)-1, raw_input().strip().split()))
    G = map(int, raw_input().strip().split())

    # pre-compute can_make_lead
    parents = defaultdict(list)
    for i in xrange(M):
        for child in R[i]:
            parents[child].append(i)
    can_make_lead = set([LEAD])
    q = deque([LEAD])
    while q:
        i = q.popleft()
        for j in parents[i]:
            if j not in can_make_lead:
                can_make_lead.add(j)
                q.append(j)

    # check if lead is reachable
    R_reach_lead = defaultdict(list)
    is_reachable = set()
    q = deque()
    for i in xrange(M):
        if not G[i]:
            continue
        is_reachable.add(i)
        R_reach_lead[i] = [child for child in R[i] if child in can_make_lead]
        q.append(i)
    while q:
        i = q.popleft()
        for j in R_reach_lead[i]:
            if j in is_reachable:
                continue
            is_reachable.add(j)
            R_reach_lead[j] = [child for child in R[j] if child in can_make_lead]
            q.append(j)
    if LEAD not in is_reachable:
        return 0

    # check if it is bounded for making leads
    if R_reach_lead[LEAD]:
        curr = LEAD
        if len(R_reach_lead[curr]) > 1:
            return "UNBOUNDED"
        curr = R_reach_lead[curr][0]
        while curr != LEAD:
            if len(R_reach_lead[curr]) > 1:
                return "UNBOUNDED"
            curr = R_reach_lead[curr][0]
        R_reach_lead[curr] = []

    # Kahn's algorithm
    indegree = defaultdict(int)
    for i in xrange(M):
        for j in R_reach_lead[i]:
            indegree[j] += 1
    totals = list(G)
    q = deque([i for i in xrange(M) if i not in indegree])
    while q:
        i = q.popleft()
        for j in R_reach_lead[i]:
            totals[j] += totals[i]
            indegree[j] -= 1
            if indegree[j] == 0:
                indegree.pop(j)
                q.append(j)
    return "UNBOUNDED" if indegree else totals[LEAD] % MOD

MOD = 10**9+7
LEAD = 0
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, contransmutation())
