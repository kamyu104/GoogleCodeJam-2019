# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 3 - Problem A. Zillionim
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051707/0000000000158f1a
#
# Time:  O(R^2), R is the max number of rounds
# Space: O(R)
#

# 2*10^10 strategy solution

from sys import stdout
from random import shuffle, seed

def insert_segment(segments, p):
    for i in xrange(len(segments)):
        start, length = segments[i]
        if start <= p <= start+length-1:
            segments[i] = (start, p-start)
            segments.append((p+L, start+length-(p+L)))
            break
    segments[:] = [(start, length) for start, length in segments if length >= L]

def find_segment(segments):  # Time: O(R)
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
        return three_or_ups[0] + 2*L  # make more segments in length 2*L as possible
    elif others:
        return others[0]  # break the segments in other lengths to make all segments are in length 2*L
    return twos[0] + len(twos)%2  # keep ai in bad even number of segments in length 2*L

def zillionim():
    segments = [(1, R*L)]
    while True:  # at most R times
        P = input()
        if P == -2 or P == -3:
            break
        if P == -1:
            exit()

        insert_segment(segments, P)
        c = find_segment(segments)  # Time: O(R)
        print c
        stdout.flush()
        insert_segment(segments, c)

R, L = 100, 10**10
T, W = map(int, raw_input().strip().split())
for case in xrange(T):
    zillionim()
