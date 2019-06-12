# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 3 - Problem B. Pancake Pyramid
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051707/00000000001591be
#
# Time:  O(S)
# Space: O(S)
#

def pancake_pyramid():
    S = input()
    P = map(int, raw_input().strip().split())

    total = 0
    stk = []
    for i, p in enumerate(P):
        while stk and stk[-1][1] <= p:
            _, h = stk.pop()
            if not stk:
                continue
            fill = ((i-1)-stk[-1][0]) * (min(stk[-1][1], p)-h)
            left, right = stk[-1][0]-0+1, (S-1)-i+1
            total += fill * left * right
        stk.append((i, p))
    return total % MOD

MOD = 10**9+7
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, pancake_pyramid())
