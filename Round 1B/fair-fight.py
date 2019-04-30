# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem C. Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
#
# Time:  O(NlogN)
# Space: O(N)
#

import collections

def lower_bound(A, curr_maxs, K):
    left, right = 0, len(curr_maxs)-1
    while left <= right:
        mid = (left + right) // 2
        if A[curr_maxs[mid]] <= K:
            right = mid-1
        else:
            left = mid+1
    return left

def fair_fight():
    N, K = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())

    L_lookup = collections.defaultdict(int)
    C_curr_maxs, D_curr_maxs = [], []
    for i in xrange(N):
        while C_curr_maxs and C[C_curr_maxs[-1]] < c:  # keep the idx where C[idx] == Ci
            C_curr_maxs.pop()
        C_L_idx = C_curr_maxs[-1]+1 if C_curr_maxs else 0  # get the leftmost idx of Ci s.t. C[idx] < Ci
        C_curr_maxs.append(i)
        while D_curr_maxs and D[D_curr_maxs[-1]] <= d:
            D_curr_maxs.pop()
        D_curr_maxs.append(i)

        if D[i]-C[i] > K:
            continue
        
        D_L_bad = lower_bound(D, D_curr_maxs, C[i]-K-1)
        D_L_good = lower_bound(D, D_curr_maxs, C[i]+K)
        D_L_bad_idx = D_curr_maxs[D_L_bad-1]+1 if D_L_bad > 0 else 0
        D_L_good_idx = D_curr_maxs[D_L_good-1]+1 if D_L_good > 0 else 0
        L_good = max(C_L_idx, D_L_good_idx)
        L_bad = max(D_L_bad_idx, L_good)

        L_lookup[i] = (L_good, L_bad)

    result = 0
    C_curr_maxs, D_curr_maxs = [], []
    for i in reversed(xrange(N)):
        while C_curr_maxs and C[C_curr_maxs[-1]] <= C[i]:
            C_curr_maxs.pop()
        C_R_idx = C_curr_maxs[-1]-1 if C_curr_maxs else N-1  # get the leftmost idx of Ci s.t. Ci >= C[idx]
        C_curr_maxs.append(i)
        while D_curr_maxs and D[D_curr_maxs[-1]] <= D[i]:
            D_curr_maxs.pop()
        D_curr_maxs.append(i)

        if D[i]-C[i] > K:
            continue

        D_R_bad = lower_bound(D, D_curr_maxs, C[i]-K-1)
        D_R_good = lower_bound(D, D_curr_maxs, C[i]+K)
        D_R_bad_idx = D_curr_maxs[D_R_bad-1]-1 if D_R_bad > 0 else N-1
        D_R_good_idx = D_curr_maxs[D_R_good-1]-1 if D_R_good > 0 else N-1
        R_good = min(C_R_idx, D_R_good_idx)
        R_bad = min(D_R_bad_idx, R_good)

        assert(i in L_lookup)
        L_good, L_bad = L_lookup[i]
        result += (i-L_good+1)*(R_good-i+1)-(i-L_bad+1)*(R_bad-i+1)

    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fair_fight())
