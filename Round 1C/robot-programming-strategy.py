# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1C - Problem A. Robot Programming Strategy
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134c90
#
# Time:  O(A^2)
# Space: O(A)
#

import collections

def robot_programming_strategy():
    A = input()
    C = []
    for _ in xrange(A):
        C.append(raw_input().strip())
    result = []
    C_remains = set(range(A))
    while C_remains:
        used = collections.defaultdict(list)
        for i in C_remains:
            used[C[i][len(result)%len(C[i])]].append(i)
            if len(used) == 3:
                return "IMPOSSIBLE"
        if len(used) == 1:
            choose = WIN_TO[used.keys().pop()]
        elif len(used) == 2:
            choose = LOSE_TO[(CHOICES-set(used.iterkeys())).pop()]  # choose the one which ties or beats another
        for i in used[LOSE_TO[choose]]:  # remove defeated opponents
            C_remains.remove(i)
        result.append(choose)
    return "".join(result)

CHOICES = set(["S", "R", "P"])
WIN_TO = {"S" : "R", "R" : "P", "P" : "S"}
LOSE_TO = {"S" : "P", "R" : "S", "P" : "R"}
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, robot_programming_strategy())
