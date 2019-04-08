# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881de
#
# Time:  O(NlogB)
# Space: O(N)
#

import sys
import functools

def encode(query, i, flip, total, valid):
    query.append(str(flip)*total)
    return valid, i

def decode(response, next_blocks, i, flip, total, valid):
    def count(response, i, c, cnt):
        same_cnt = 0
        while i < len(response) and same_cnt < cnt:
            if response[i] == c:
                same_cnt += 1
            else:
                break
            i += 1
        return same_cnt, i
    
    used_valid, i = count(response, i, flip, valid)
    next_blocks.append((total, used_valid))
    return used_valid, i

def init_codec(N, total, callback):
    # split N into blocks with size "total"
    i = 0
    cnt, flip = N, 0
    while cnt > total:
        used_valid, i = callback(i, flip, total, total)
        cnt -= total
        flip ^= 1
    used_valid, i = callback(i, flip, cnt, cnt)

def codec(blocks, callback):
    i = 0
    is_done = True
    for total, valid in blocks:
        if total == valid or valid == 0:
            used_valid, i = callback(i, 0, total, valid)
        else:
            # equally split each block into 2 blocks.
            # after ceil(log2(B)) times splits,
            # each block must converge into size 1 or stop split
            is_done = False
            used_valid, i = callback(i, 0, total//2, valid)
            used_valid, i = callback(i, 1, (total+1)//2, valid-used_valid)
    return is_done

def dat_bae():
    N, B, F = map(int, raw_input().strip().split())

    # ceil(log2(B)) + 1 <= F
    # => B <= min(15, N-1)
    # => ceil(log2(B)) + 1 <= 5 = F
    
    # find the smallest Q s.t. 2**Q >= B
    # p.s. if 2**Q < B, when the whole 2**Q block is missing,
    #      we cannot tell which block is lost
    Q = 0
    while 2**Q < B:
        Q += 1
    assert(Q+1<=F)
    # if 2**Q == N, in order to save a query,
    # we can just skip init_codec and begin with block (N, N-B)
    blocks = [] if 2**Q < N else [(N, N-B)]
    while Q >= 0:  # at most ceil(log2(B)) + 1 times
        query = []
        query_callback = functools.partial(encode, query)
        if not blocks:
            init_codec(N, 2**Q, query_callback)
        else:
            is_done = codec(blocks, query_callback)
            if is_done: break

        print "".join(query)
        sys.stdout.flush()
        response = map(int, raw_input())

        next_blocks = []
        response_callback = functools.partial(decode, response, next_blocks)
        if not blocks:
            init_codec(N, 2**Q, response_callback)
        else: 
            codec(blocks, response_callback)
        blocks, next_blocks = next_blocks, blocks

        # print >> sys.stderr, blocks
        Q -= 1

    result, i = [], 0
    for total, valid in blocks:
        if valid == 0:
            for j in xrange(i, i+total):
                result.append(str(j))
        i += total

    print " ".join(result)
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

for case in xrange(input()):
    dat_bae()
