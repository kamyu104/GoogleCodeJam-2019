# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem A. Foregone Solution
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
#
# Time:  O(logN)
# Space: O(1)
#

def foregone_solution():
    N = raw_input()
    A, B = [], []
    for d in N:
        if d == '4':
            A.append('2')
            B.append('2')
        else:
            A.append(d)
            if B: B.append('0')
    return "{} {}".format("".join(A), "".join(B))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, foregone_solution())
