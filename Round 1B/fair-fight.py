# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem C. Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
#
# Time:  O(NlogN)
# Space: O(N)
#

import collections

def lower_bound(A, curr_max_idxs, K):
    left, right = 0, len(curr_max_idxs)-1
    while left <= right:
        mid = (left + right) // 2
        if A[curr_max_idxs[mid]] <= K:
            right = mid-1
        else:
            left = mid+1
    return left

def fair_fight():
    N, K = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())

    L_lookup = collections.defaultdict(int)
    C_curr_max_idxs, D_curr_max_idxs = [], []
    for i in xrange(N):
        while C_curr_max_idxs and C[C_curr_max_idxs[-1]] < C[i]:  # keep the idx where C[idx] == Ci
            C_curr_max_idxs.pop()
        C_curr_max_idxs.append(i)
        while D_curr_max_idxs and D[D_curr_max_idxs[-1]] <= D[i]:
            D_curr_max_idxs.pop()
        D_curr_max_idxs.append(i)

        if D[i]-C[i] > K:
            continue
        
        C_L = C_curr_max_idxs[-2]+1 if len(C_curr_max_idxs) >= 2 else 0  # get the leftmost idx of Ci s.t. C[idx] < Ci
        D_L_good_it = lower_bound(D, D_curr_max_idxs, C[i]+K)
        D_L_bad_it = lower_bound(D, D_curr_max_idxs, C[i]-K-1)
        D_L_good = D_curr_max_idxs[D_L_good_it-1]+1 if D_L_good_it > 0 else 0
        D_L_bad = D_curr_max_idxs[D_L_bad_it-1]+1 if D_L_bad_it > 0 else 0
        L_good = max(C_L, D_L_good)
        L_bad = max(L_good, D_L_bad)

        L_lookup[i] = (L_good, L_bad)

    result = 0
    C_curr_max_idxs, D_curr_max_idxs = [], []
    for i in reversed(xrange(N)):
        while C_curr_max_idxs and C[C_curr_max_idxs[-1]] <= C[i]:
            C_curr_max_idxs.pop()
        C_curr_max_idxs.append(i)
        while D_curr_max_idxs and D[D_curr_max_idxs[-1]] <= D[i]:
            D_curr_max_idxs.pop()
        D_curr_max_idxs.append(i)

        if D[i]-C[i] > K:
            continue

        C_R = C_curr_max_idxs[-2]-1 if len(C_curr_max_idxs) >= 2 else N-1  # get the rightmost idx of Ci s.t. Ci >= C[idx]
        D_R_good_it = lower_bound(D, D_curr_max_idxs, C[i]+K)
        D_R_bad_it = lower_bound(D, D_curr_max_idxs, C[i]-K-1)
        D_R_good = D_curr_max_idxs[D_R_good_it-1]-1 if D_R_good_it > 0 else N-1
        D_R_bad = D_curr_max_idxs[D_R_bad_it-1]-1 if D_R_bad_it > 0 else N-1
        R_good = min(C_R, D_R_good)
        R_bad = min(R_good, D_R_bad)

        assert(i in L_lookup)
        L_good, L_bad = L_lookup[i]
        result += (i-L_good+1)*(R_good-i+1)-(i-L_bad+1)*(R_bad-i+1)

    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fair_fight())
