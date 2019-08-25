# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem #. Juggle Struggle: Part 2
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c933
#
# Time:  O(N^2), TLE in test set 2
# Space: O(N)
#

# Computes the cross product of vectors AB and AC
CW, COLINEAR, CCW = range(-1, 2)
def ccw(A, B, C):
    area = (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
    return CCW if area > 0 else CW if area < 0 else COLINEAR

# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def juggle_struggle_part2():
    N = input()
    P = [None]*N
    for i in xrange(len(P)):
        X1, Y1, X2, Y2 = map(int, raw_input().strip().split())
        P[i] = [(X1, Y1), (X2, Y2)]

    result = []
    lookup = set()
    for i in xrange(len(P)-1):
        for j in xrange(i+1, len(P)):
            if intersect(P[i][0], P[i][1], P[j][0], P[j][1]):
                continue
            lookup.add(i)
            lookup.add(j)
        if i in lookup:
            result.append(i)
    return " ".join(map(str, map(lambda x: x+1, result))) if result else "MAGNIFICENT"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, juggle_struggle_part2())
