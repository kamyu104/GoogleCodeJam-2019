# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#
# Time:  O(NlogB)
# Space: O(NlogB)
#

import sys

def set_idx(queries, i, idx):
    for j in xrange(len(queries)):
        queries[j][i] = (idx>>j)&1
        
def get_idx(responses, i):
    cur_idx = 0
    for j in xrange(len(responses)):
        cur_idx |= (responses[j][i])<<j
    return cur_idx

def dat_bae():
    N, B, F = map(int, raw_input().strip().split())

    # find the smallest Q s.t. 2**Q > B
    Q = 1
    while 2**Q <= B:
        Q += 1
    assert(Q <= F)
    queries = [[0 for _ in xrange(N)] for _ in xrange(Q)]  # floor(log2(B)) + 1 times
    for i in xrange(N):
        set_idx(queries, i, i % (2**Q))
    for q in queries:
        print "".join(map(str, q))
    sys.stdout.flush()

    responses = [map(int, raw_input()) for _ in xrange(Q)]

    result = []
    i = 0
    for idx in xrange(N):
        if get_idx(responses, i) != (idx % (2**Q)) :
            result.append(str(idx))
        elif i+1 < N-B:
            i += 1

    print " ".join(result)
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

for case in xrange(input()):
    dat_bae()
