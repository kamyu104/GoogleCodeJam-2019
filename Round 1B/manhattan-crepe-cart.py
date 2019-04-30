# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem A. Manhattan Crepe Cart
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c
#
# Time:  O(PlogP)
# Space: O(P)

import collections

def choose(lookup):
    positions = list(lookup.iteritems())
    positions.sort()
    result, max_votes = None, float("-inf")
    curr_pos, curr_votes = 0, 0
    for pos, v in positions:
        if pos > curr_pos:
            if curr_votes > max_votes:
                max_votes = curr_votes
                result = curr_pos
            curr_pos = pos
        curr_votes += v
    return result

def manhattan_crepe_cart():
    P, Q = map(int, raw_input().strip().split())
    lookup_X, lookup_Y = collections.defaultdict(int), collections.defaultdict(int)
    lookup_X[Q+1], lookup_Y[Q+1] = 0, 0
    for _ in xrange(P):
        X, Y, D = raw_input().strip().split()
        X, Y = int(X), int(Y)
        if D == "E":
            lookup_X[X+1] += 1
        elif D == "W":
            lookup_X[X] -= 1
        elif D in "N":
            lookup_Y[Y+1] += 1
        elif D in "S":
            lookup_Y[Y] -= 1
    
    return "{} {}".format(choose(lookup_X), choose(lookup_Y))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, manhattan_crepe_cart())
