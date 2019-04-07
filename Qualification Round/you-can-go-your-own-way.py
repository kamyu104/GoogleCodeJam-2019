# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem B. You Can Go Your Own Way
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
#
# Time:  O(N)
# Space: O(1)
#

def you_can_go_your_own_way():
    N = input()
    P = raw_input()
    result = []
    for move in P:
        result.append('E' if move == 'S' else 'S')
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, you_can_go_your_own_way())
