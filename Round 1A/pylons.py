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

def pylons2():
    R, C = map(int, raw_input().strip().split())

    swapped = False
    if R > C:
        R, C = C, R
        swapped = True

    result = []
    r = 0
    if C >= 4:
        while (R-r) >= 3 and (R-r) != 4:  # case 3 rows
            iter3 = begin_at_i_seq(C, 1)
            iter2 = begin_at_i_seq(C, 3)
            iter1 = begin_at_i_seq(C, 1)
            for c in xrange(C):
                result.append((r+3, next(iter3)))
                result.append((r+2, next(iter2)))
                result.append((r+1, next(iter1)))
            r += 3

        if (R-r) == 4:  # case 4 rows
            iter4 = begin_at_i_seq(C, 3)
            iter3 = begin_at_i_seq(C, 1)
            iter2 = begin_at_i_seq(C, 3)
            iter1 = begin_at_i_seq(C, 1)
            for c in xrange(C):
                result.append((r+4, next(iter4)))
                result.append((r+3, next(iter3)))
                result.append((r+2, next(iter2)))
                result.append((r+1, next(iter1)))
                if len(result) >= 5 and abs(result[-5][0]-result[-4][0]) == abs(result[-5][1]-result[-4][1]):
                    result[-4], result[-2] = result[-2], result[-4]
            r += 4
        elif (R-r) == 2 and C >= 5:  # case 2 rows
            iter2 = begin_at_i_seq(C, 3)
            iter1 = begin_at_i_seq(C, 1)
            for _ in xrange(C):
                result.append((r+2, next(iter2)))
                result.append((r+1, next(iter1)))
            r += 2

    if r != R:
        return "IMPOSSIBLE"

    if swapped:
        swapped = False
        for i in xrange(len(result)):
            result[i] = (result[i][1], result[i][0])
        R, C = C, R

    assert(R*C == len(result))
    for i in xrange(1, len(result)):
        assert((abs(result[i][0]-result[i-1][0]) != abs(result[i][1]-result[i-1][1]) and
               result[i][0]-result[i-1][0] != 0 and result[i][1]-result[i-1][1] != 0))

    return "POSSIBLE\n{}".format("\n".join(map(lambda x: " ".join(map(str, x)), result)))

def pylons():
    R, C = map(int, raw_input().strip().split())

    swapped = False
    if R > C:
        R, C = C, R
        swapped = True

    result = []
    r = 0
    if C >= 4:
        while (R-r) >= 4 and (R-r) != 5:  # case 4 rows
            iter4 = begin_at_i_seq(C, 3)
            iter3 = begin_at_i_seq(C, 1)
            iter2 = begin_at_i_seq(C, 3)
            iter1 = begin_at_i_seq(C, 1)
            for c in xrange(C):
                result.append((r+4, next(iter4)))
                result.append((r+3, next(iter3)))
                result.append((r+2, next(iter2)))
                result.append((r+1, next(iter1)))
                if len(result) >= 5 and abs(result[-5][0]-result[-4][0]) == abs(result[-5][1]-result[-4][1]):
                    result[-4], result[-2] = result[-2], result[-4]
            r += 4
            
        while (R-r) >= 3:  # case 3 rows
            iter3 = begin_at_i_seq(C, 1)
            iter2 = begin_at_i_seq(C, 3)
            iter1 = begin_at_i_seq(C, 1)
            for c in xrange(C):
                result.append((r+3, next(iter3)))
                result.append((r+2, next(iter2)))
                result.append((r+1, next(iter1)))
            r += 3

        if (R-r) == 2 and C >= 5:  # case 2 rows
            iter2 = begin_at_i_seq(C, 3)
            iter1 = begin_at_i_seq(C, 1)
            for _ in xrange(C):
                result.append((r+2, next(iter2)))
                result.append((r+1, next(iter1)))
            r += 2

    if r != R:
        return "IMPOSSIBLE"

    if swapped:
        swapped = False
        for i in xrange(len(result)):
            result[i] = (result[i][1], result[i][0])
        R, C = C, R

    assert(R*C == len(result))
    for i in xrange(1, len(result)):
        assert((abs(result[i][0]-result[i-1][0]) != abs(result[i][1]-result[i-1][1]) and
               result[i][0]-result[i-1][0] != 0 and result[i][1]-result[i-1][1] != 0))

    return "POSSIBLE\n{}".format("\n".join(map(lambda x: " ".join(map(str, x)), result)))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, pylons())
