# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem E. Juggle Struggle: Part 2
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c933
#
# Time:  O(NlogN)
# Space: O(N)
#

from itertools import islice

# Computes the cross product of vectors AB and AC
CW, COLINEAR, CCW = range(-1, 2)
def ccw(A, B, C):
    area = (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])
    return CCW if area > 0 else CW if area < 0 else COLINEAR

# Return true if line segments AB and CD intersect
def intersect(A, B, C, D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# Return the intersection of AB and CD if it exists
def find_intersection(A, B, C, D):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    px, py = None, None
    detC = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if detC:
        detA, detB = (x1*y2-y1*x2)*(x3-x4), (x3*y4-y3*x4)
        px = (detA-(x1-x2)*detB)*1.0/detC
        py = (detA-(y1-y2)*detB)*1.0/detC
    return [px, py]

def reflect_across_x(p):
    return (p[0], -p[1])

def reflect_across_y(p):
    return (-p[0], p[1])

def find_leftmost_below(L, F):
    if not L:
        return

    X0 = min(min(l[1][0], l[2][0]) for l in L)
    L.sort(reverse=True, key=lambda x: find_intersection(x[1], x[2], (X0, 0), (X0, 1))[1])
    X1 = max(max(l[1][0], l[2][0]) for l in L)
    stk = [(0, X1)]
    for i, (idx, A, B) in enumerate(islice(L, 1, len(L)), 1):
        while True:
            _, C, D = L[stk[-1][0]]
            X = find_intersection(A, B, C, D)[0]
            if not (X is not None and
                    min(A[0], B[0]) <= X <= max(A[0], B[0]) and
                    min(C[0], D[0]) <= X <= max(C[0], D[0])):
                F.add(idx)
                break
            if not (len(stk) >= 2 and stk[-1][1] <= X):
                break
            stk.pop()
        if idx in F:
            continue
        stk.append((i, X))  # only keep valid X in stk       

def juggle_struggle_part2():
    N = input()
    L = [None]*N
    V = []
    for i in xrange(len(L)):
        X1, Y1, X2, Y2 = map(int, raw_input().strip().split())
        if X1 == X2:
            V.append(i)
        L[i] = [i, (X1, Y1), (X2, Y2)]

    F = set()
    if len(V) > 1:  # more than 1 vertical lines
        F = set(V)
    elif len(V) == 1:  # only 1 vertical line
        idx, A, B = L[V[0]]
        for j, C, D in L:
            if j == idx:
                continue
            if not intersect(A, B, C, D):
                F.add(idx)

    for leftmost in [True, False]:
        for below in [True, False]:
            l = [l for l in L if l[0] not in F]
            if not leftmost:
                l = map(lambda x: [x[0], reflect_across_y(x[1]), reflect_across_y(x[2])], l)
            if not below:
                l = map(lambda x: [x[0], reflect_across_x(x[1]), reflect_across_x(x[2])], l)
            find_leftmost_below(l, F)

    for f in list(F):  # at most 25 by limit constraint
        i, A, B = L[f]
        for idx, C, D in L:
            if i == idx:
                continue
            if not intersect(A, B, C, D):
                F.add(idx)
    result = [i+1 for i in xrange(len(L)) if i in F]
    return "MAGNIFICENT" if not result else " ".join(map(str, result))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, juggle_struggle_part2())
