# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1C - Problem C. Bacterial Tactics
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134cdf
#
# Time:  O(R^3 * C^3)
# Space: O(R^2 * C^2)
#

def mex(s):  # minimum excludant
    excludant = 0
    while excludant in s:
        excludant += 1
    return excludant

def grundy(M, r0, c0, r1, c1, lookup):  # Time:  O(R + C)
    result = 0
    if r0 == r1 or c0 == c1:
        return 0, result
    if (r0, c0, r1, c1) not in lookup:
        s = set()
        # horizontal
        for r in xrange(r0, r1):  # Time:  O(R)
            for c in xrange(c0, c1):
                if M[r][c] == '#':
                    break
            else:
                g = grundy(M, r0, c0, r, c1, lookup)[0] ^ \
                    grundy(M, r+1, c0, r1, c1, lookup)[0]
                s.add(g)
                if not g:
                    result += c1-c0
        # vertical
        for c in xrange(c0, c1):  # Time:  O(C)
            for r in xrange(r0, r1):
                if M[r][c] == '#':
                    break
            else:
                g = grundy(M, r0, c0, r1, c, lookup)[0] ^ \
                    grundy(M, r0, c+1, r1, c1, lookup)[0]
                s.add(g)
                if not g:
                    result += r1-r0
        lookup[r0, c0, r1, c1] = mex(s)  # Time:  O(R + C)
    return lookup[r0, c0, r1, c1], result

def bacterial_tactics():
    R, C = map(int, raw_input().strip().split())
    M = []
    for _ in xrange(R):
        M.append(list(raw_input().strip()))

    g, result = grundy(M, 0, 0, R, C, {})
    return result if g else 0

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, bacterial_tactics())
