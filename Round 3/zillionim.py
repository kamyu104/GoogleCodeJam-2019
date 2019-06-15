# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 3 - Problem A. Zillionim
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051707/0000000000158f1a
#
# Time:  O(R^2), R is the max number of rounds
# Space: O(R)
#
# python interactive_runner.py python testing_tool.py 2 -- python zillionim.py
#

from sys import stdout
from random import shuffle, seed

def insert_segment(segments, p):
    for i in xrange(len(segments)):
        start, length = segments[i]
        if start <= p <= start+length-1:
            segments[i] = start, p-start
            segments.append((p+L, start+length-(p+L)))
            break
    return [(start, length) for start, length in segments if length >= L]

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
        for p, length in segments:
            if length >= 3*L:
                three_or_ups.append(p)
            elif length == 2*L:
                twos.append(p)
            else:
                others.append(p)

        seed(4)  # tuned by testing_tool.py, and it also passed the online judge
        map(shuffle, [three_or_ups, twos, others])
        if three_or_ups:
            p = three_or_ups[0]
            c = p + 2*L  # make more segments in length 2*L as possible
        elif others:
            c = others[0]  # break the segments in other lengths to make all segments are in length 2*L
        else:
            p = twos[0]
            c = p + len(twos)%2  # keep ai in bad even number of segments in length 2*L

        segments = insert_segment(segments, c)
        print c
        stdout.flush()

R, L = 100, 10**10
T, W = map(int, raw_input().strip().split())
for case in xrange(T):
    zillionim()
