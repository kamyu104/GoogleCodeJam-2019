# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem A. Manhattan Crepe Cart
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/000000000012295c
#
# Time:  O(PlogP)
# Space: O(P)

import collections

def choose(lookup, L, R):
    positions = []
    for k, v in lookup.iteritems():
        positions.append((k, v[L], v[R]))
    positions.sort()
    candidate, votes = 0, sum(v[L] for v in lookup.itervalues())
    max_votes = votes
    for i, (pos, left, right) in enumerate(positions):
        votes += right
        votes -= left if pos-1 not in lookup else 0  # to avoid subtracting twice
        votes -= lookup[pos+1][L] if pos+1 in lookup else 0
        if votes > max_votes:
            candidate, max_votes = pos+1, votes
    return candidate

def manhattan_crepe_cart():
    P, Q = map(int, raw_input().strip().split())
    lookup_X = collections.defaultdict(lambda:collections.defaultdict(int))
    lookup_X[0]
    lookup_Y = collections.defaultdict(lambda:collections.defaultdict(int))
    lookup_Y[0]
    for _ in xrange(P):
        X, Y, D = raw_input().strip().split()
        X, Y = int(X), int(Y)
        if D in "EW":
            lookup_X[X][D] += 1
        elif D in "SN":
            lookup_Y[Y][D] += 1
    
    return "{} {}".format(choose(lookup_X, "W", "E"),
                          choose(lookup_Y, "S", "N"))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, manhattan_crepe_cart())
