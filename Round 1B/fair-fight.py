# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem C. Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
#
# Time:  O(NlogN)
# Space: O(N)
#

def update_strictly_descending_stack(A, idxs, i):
    while idxs and A[idxs[-1]] <= A[i]:
        idxs.pop()
    idxs.append(i)
    
def update_descending_stack(A, idxs, i):
    while idxs and A[idxs[-1]] < A[i]:
        idxs.pop()
    idxs.append(i)

def lower_bound(A, curr_max_idxs, K):
    left, right = 0, len(curr_max_idxs)-1
    while left <= right:
        mid = left + (right-left)//2
        if A[curr_max_idxs[mid]] <= K:
            right = mid-1
        else:
            left = mid+1
    return left

def fair_fight():
    N, K = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())

    R_lookup = []
    C_curr_max_idxs, D_curr_max_idxs = [], []  # descending stack
    for i in reversed(xrange(N)):
        update_strictly_descending_stack(C, C_curr_max_idxs, i)
        update_strictly_descending_stack(D, D_curr_max_idxs, i)
        
        if D[i]-C[i] > K:  # skip impossible intervals to save time and space
            continue
        D_R_good_it = lower_bound(D, D_curr_max_idxs, C[i]+K)
        D_R_bad_it = lower_bound(D, D_curr_max_idxs, C[i]-K-1)
        D_R_good = D_curr_max_idxs[D_R_good_it-1]-1 if D_R_good_it > 0 else N-1  # rightmost idx of max_D s.t. max_D-Ci <= K
        D_R_bad = D_curr_max_idxs[D_R_bad_it-1]-1 if D_R_bad_it > 0 else N-1  # rightmost idx of max_D s.t. max_D-Ci <= -K-1
        C_R = C_curr_max_idxs[-2]-1 if len(C_curr_max_idxs) >= 2 else N-1  # rightmost idx of C s.t. Ci >= C[idx]
        R_good, R_bad = min(D_R_good, C_R), min(D_R_bad, C_R)

        R_lookup.append((R_good, R_bad))

    result = 0
    C_curr_max_idxs, D_curr_max_idxs = [], []  # descending stack
    for i in xrange(N):
        update_descending_stack(C, C_curr_max_idxs, i)  # keep the idx where C[idx] == Ci
        update_strictly_descending_stack(D, D_curr_max_idxs, i)
        
        if D[i]-C[i] > K:  # skip impossible intervals to save time and space
            continue
        D_L_good_it = lower_bound(D, D_curr_max_idxs, C[i]+K)
        D_L_bad_it = lower_bound(D, D_curr_max_idxs, C[i]-K-1)
        D_L_good = D_curr_max_idxs[D_L_good_it-1]+1 if D_L_good_it > 0 else 0  # leftmost idx of max_D s.t. max_D-Ci <= K
        D_L_bad = D_curr_max_idxs[D_L_bad_it-1]+1 if D_L_bad_it > 0 else 0  # leftmost idx of max_D s.t. max_D-Ci <= -K-1
        C_L = C_curr_max_idxs[-2]+1 if len(C_curr_max_idxs) >= 2 else 0  # leftmost idx of C s.t. C[idx] < Ci
        L_good, L_bad = max(D_L_good, C_L), max(D_L_bad, C_L)

        R_good, R_bad = R_lookup.pop()
        result += (i-L_good+1)*(R_good-i+1)-(i-L_bad+1)*(R_bad-i+1)

    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fair_fight())
