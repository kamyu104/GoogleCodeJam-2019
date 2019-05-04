# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1C - Problem C. Bacterial Tactics
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134cdf
#
# Time:  O(R^2 * C^2 * (R + C))
# Space: O(R^2 * C^2)
#

def mex(s):  # minimum excludant
    excludant = 0
    while excludant in s:
        excludant += 1
    return excludant

def grundy(RC, r0, c0, r1, c1, lookup):  # there are O(R^2 * C^2) subproblems, each costs O(R + C) time
    result = 0
    if r0 == r1 or c0 == c1:
        return 0, result

    if (r0, c0, r1, c1) not in lookup:
        s = set()
        # horizontal check
        for r in xrange(r0, r1):  # Time:  O(R)
            if c0 <= RC[LEFT][r][c0] or RC[RIGHT][r][c0] < c1:  # nearest radioactive cell in the same row
                continue
            g = grundy(RC, r0, c0, r, c1, lookup)[0] ^ \
                grundy(RC, r+1, c0, r1, c1, lookup)[0]
            s.add(g)
            if not g:  # if the opponent loses
                result += c1-c0

        # vertical check
        for c in xrange(c0, c1):  # Time:  O(C)
            if r0 <= RC[UP][r0][c] or RC[DOWN][r0][c] < r1:  # nearest radioactive cell in the same column
                continue
            g = grundy(RC, r0, c0, r1, c, lookup)[0] ^ \
                grundy(RC, r0, c+1, r1, c1, lookup)[0]
            s.add(g)
            if not g:  # if the opponent loses
                result += r1-r0
        lookup[r0, c0, r1, c1] = mex(s)  # Time:  O(R + C)

    return lookup[r0, c0, r1, c1], result

def bacterial_tactics():
    R, C = map(int, raw_input().strip().split())
    M = []
    for _ in xrange(R):
        M.append(list(raw_input().strip()))

    # nearest radioactive cell from left, right, up, down
    RC = [[[None for _ in xrange(C)] for _ in xrange(R)] for _ in xrange(4)]
    for r in xrange(R):
        radio_cell = -1
        for c in xrange(C):
            if M[r][c] == '#':
                radio_cell = c
            RC[LEFT][r][c] = radio_cell
        radio_cell = C
        for c in reversed(xrange(C)):
            if M[r][c] == '#':
                radio_cell = c
            RC[RIGHT][r][c] = radio_cell
    for c in xrange(C):
        radio_cell = -1
        for r in xrange(R):
            if M[r][c] == '#':
                radio_cell = r
            RC[UP][r][c] = radio_cell
        radio_cell = R
        for r in reversed(xrange(R)):
            if M[r][c] == '#':
                radio_cell = r
            RC[DOWN][r][c] = radio_cell

    g, result = grundy(RC, 0, 0, R, C, {})
    return result if g else 0

LEFT, RIGHT, UP, DOWN = range(4)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bacterial_tactics())
