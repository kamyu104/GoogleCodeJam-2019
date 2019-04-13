# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1A - Problem A. Pylons
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e03
#
# Time:  O(R * C)
# Space: O(1)
#

def begin_at_i_seq(C, i):
    for c in xrange(i, C+1):
        yield c
    for c in xrange(1, i):
        yield c

def reverse_after_i_seq(C, i):
    for c in xrange(1, i):
        yield c
    for c in reversed(xrange(i, C+1)):
        yield c

def pylons():
    R, C = map(int, raw_input().strip().split())

    swapped = False
    if R > C:
        R, C = C, R
        swapped = True

    result = []
    r = 0
    if R >= 3 and C >= 4:
        if R % 4 == 0:  # 4k+4
            while r != R:
                iter1 = begin_at_i_seq(C, 1)
                iter2 = begin_at_i_seq(C, 3)
                iter3 = begin_at_i_seq(C, 1)
                iter4 = begin_at_i_seq(C, 3)
                for c in xrange(C):
                    result.append((r+1, next(iter1)))
                    result.append((r+2, next(iter2)))
                    result.append((r+3, next(iter3)))
                    result.append((r+4, next(iter4)))
                    if len(result) >= 5 and abs(result[-5][0]-result[-4][0]) == abs(result[-5][1]-result[-4][1]):
                        result[-4], result[-2] = result[-2], result[-4]
                r += 4
        elif R % 2 != 0:  # 2k+3
            iter1 = begin_at_i_seq(C, 1)
            iter2 = begin_at_i_seq(C, 3)
            iter3 = begin_at_i_seq(C, 1)
            for c in xrange(C):
                result.append((r+1, next(iter1)))
                result.append((r+2, next(iter2)))
                result.append((r+3, next(iter3)))
            r += 3

    if (R-r) % 2 == 0 and C >= 5:  # 2k+2
        while r != R:
            r1, r2 = r+1, r+2
            if result and abs(r1 - result[-1][0]) == abs(3 - result[-1][1]):
                r1, r2 = r2, r1
            iter1 = begin_at_i_seq(C, 3)
            iter2 = reverse_after_i_seq(C, C-1)
            for _ in xrange(C):
                result.append((r1, next(iter1)))
                result.append((r2, next(iter2)))
            r += 2

    if r != R:
        return "IMPOSSIBLE"

    if swapped:
        swapped = False
        for i in xrange(len(result)):
            result[i] = (result[i][1], result[i][0])
        R, C = C, R

    return "POSSIBLE\n{}".format("\n".join(map(lambda x: " ".join(map(str, x)), result)))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, pylons())
