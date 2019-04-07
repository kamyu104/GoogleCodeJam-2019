# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem D. Dat Bae
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#
# Time:  O(NlogB)
# Space: O(N)
#

import sys
import functools

def encode(query, i, flip, total, valid):
    query.append(str(flip)*total)
    return valid, i

def decode(next_segments, response, i, flip, total, valid):
    def count(response, i, c, cnt):
        same_cnt = 0
        while i < len(response) and same_cnt < cnt:
            if response[i] == c:
                same_cnt += 1
            else:
                break
            i += 1
        return same_cnt, i
    
    used_valid, i = count(response, i, str(flip), valid)
    next_segments.append((total, used_valid))
    return used_valid, i

def init_codec(N, total, callback):
    # split N into segments with size "total"
    i = 0
    cnt, flip = N, 0
    while cnt > total:
        used_valid, i = callback(i, flip, total, total)
        cnt -= total
        flip ^= 1
    used_valid, i = callback(i, flip, cnt, cnt)

def codec(segments, callback):
    i = 0
    is_done = True
    for total, valid in segments:
        if total == valid or valid == 0:
            used_valid, i = callback(i, 0, total, valid)
        else:
            # equally split each segment into 2 segments
            is_done = False
            used_valid, i = callback(i, 0, total//2, valid)
            used_valid, i = callback(i, 1, (total+1)//2, valid-used_valid)
    return is_done

def dat_bae():
    N, B, F = map(int, raw_input().strip().split())

    # ceil(log2(B)) + 1 <= F
    # => B <= min(15, N-1)
    # => ceil(log2(B)) + 1 <= 5 = F
    
    # find the smalleset value of size >= B
    size = 1
    while size < B:
        size *= 2
    
    segments = [] if size < N else [(N, N-B)]
    while size:  # min(ceil(log2(N-1)), ceil(log2(B)) + 1) times
        query = []
        if not segments:
            init_codec(N, size, functools.partial(encode, query))
        else:
            is_done = codec(segments, functools.partial(encode, query))
            if is_done: break

        print "".join(query)
        sys.stdout.flush()
        response = list(raw_input().strip().split()[0])

        next_segments = []
        if not segments:
            init_codec(N, size, functools.partial(decode, next_segments, response))
        else: 
            codec(segments, functools.partial(decode, next_segments, response))
        segments, next_segments = next_segments, segments
        size //= 2

    result, i = [], 0
    for total, valid in segments:
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
