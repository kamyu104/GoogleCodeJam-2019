# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem C. Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
#
# Time:  O(NlogN)
# Space: O(N)
#

import collections

def lower_bound(A, intervals, left, right, K):
    while left <= right:
        mid = (left + right) // 2
        if A[intervals[mid]] <= K:
            right = mid-1
        else:
            left = mid+1
    return left

def fair_fight():
    N, K = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())

    L_lookup, R_lookup = collections.defaultdict(int), collections.defaultdict(int)
    C_intervals, D_intervals = [None]*(N+1), [None]*(N+1)

    C_intervals_valid, D_intervals_valid = -1, -1
    for i in xrange(N):
        c, d = C[i], D[i]

        L_C = lower_bound(C, C_intervals, 0, C_intervals_valid, c-1)
        C_intervals[L_C],  C_intervals_valid = i, L_C
        L_D = lower_bound(D, D_intervals, 0, D_intervals_valid, d)
        D_intervals[L_D], D_intervals_valid = i, L_D

        if d-c > K:
            continue

        C_L_idx = C_intervals[L_C-1]+1 if L_C > 0 else 0
        D_L_bad = lower_bound(D, D_intervals, 0, D_intervals_valid, c-K-1)
        D_L_good = lower_bound(D, D_intervals, 0, D_intervals_valid, c+K)
        D_L_bad_idx = D_intervals[D_L_bad-1] if D_L_bad > 0 else -1
        D_L_good_idx = D_intervals[D_L_good-1]+1 if D_L_good > 0 else 0
        L_good_idx = max(C_L_idx, D_L_good_idx)
        L_bad_idx = max(D_L_bad_idx+1, L_good_idx)
        L_lookup[i] = (L_good_idx, L_bad_idx)

    C_intervals_valid, D_intervals_valid = -1, -1
    for i in reversed(xrange(N)):
        c, d = C[i], D[i]

        R_C = lower_bound(C, C_intervals, 0, C_intervals_valid, c)
        C_intervals[R_C], C_intervals_valid = i, R_C
        R_D = lower_bound(D, D_intervals, 0, D_intervals_valid, d)
        D_intervals[R_D], D_intervals_valid = i, R_D

        if d-c > K:
            continue

        C_R_idx = C_intervals[R_C-1]-1 if R_C > 0 else N-1
        D_R_bad = lower_bound(D, D_intervals, 0, D_intervals_valid, c-K-1)
        D_R_good = lower_bound(D, D_intervals, 0, D_intervals_valid, c+K)
        D_R_bad_idx = D_intervals[D_R_bad-1] if D_R_bad > 0 else N
        D_R_good_idx = D_intervals[D_R_good-1]-1 if D_R_good > 0 else N-1
        R_good_idx = min(C_R_idx, D_R_good_idx)
        R_bad_idx = min(D_R_bad_idx-1, R_good_idx)
        R_lookup[i] = (R_good_idx, R_bad_idx)

    result = 0
    for i in xrange(N):
        if i not in L_lookup or i not in R_lookup:
            continue
        L_good, L_bad = L_lookup[i]
        R_good, R_bad = R_lookup[i]
        result += (i-L_good+1)*(R_good-i+1)-(i-L_bad+1)*(R_bad-i+1)
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fair_fight())

