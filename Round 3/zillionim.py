# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 3 - Problem A. Zillionim
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051707/0000000000158f1a
#
# Time:  O(R^2), R is the max number of rounds
# Space: O(R)
#

import sys

def insert_segment(segments, p):
    for i in xrange(len(segments)):
        x, y = segments[i]
        if x <= p <= y:
            segments[i] = x, p - 1
            segments.append((p + L, y))
            break
    return [(x, y) for x, y in segments if y - x + 1 >= L]

def zillionim():
    segments = [(1, R*L)]
    while True:
        P = input()
        if P == -2 or P == -3:
            break
        if P == -1:
            exit()

        segments = insert_segment(segments, P)
        three_or_ups, twos, others = [], [], []
        for x, y in segments:
            d = y - x + 1
            if d >= 3*L:
                three_or_ups.append((x, y))
            elif d == 2*L:
                twos.append((x, y))
            else:
                others.append((x, y))

        if three_or_ups:
            x, y = three_or_ups[0]
            c = x + 2*L  # make more segments in length 2*L as possible
        elif others:
            x, y = others[0]  # break the segments in other lengths to make all segments are in length 2*L
            c = x
        else:
            x, y = twos[0]
            c = x + len(twos)%2  # keep ai in bad even number of segments in length 2*L

        segments = insert_segment(segments, c)
        print c
        sys.stdout.flush()

R, L = 100, 10**10
T, W = map(int, raw_input().strip().split())
for case in xrange(T):
    zillionim()
