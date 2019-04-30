# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem B. Draupnir
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122837
#
# Time:  O(1)
# Space: O(1)
#

import sys

def draupnir():
    Q = Q1  # 190
    print Q
    sys.stdout.flush()
    N = input()
    R4 = (N>>(Q//4))
    R5 = (N>>(Q//5)) & ((1<<R.bit_length())-1)
    R6 = (N>>(Q//6)) & ((1<<R.bit_length())-1)

    Q = Q2  # 38
    print Q
    sys.stdout.flush()
    N = input()
    N -= R4 * 2**(Q//4) + R5 * 2**(Q//5) + R6 * 2**(Q//6)
    R1 = (N>>(Q//1))
    R2 = (N>>(Q//2)) & ((1<<R.bit_length())-1)
    R3 = (N>>(Q//3)) & ((1<<R.bit_length())-1)

    print R1, R2, R3, R4, R5, R6
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

R = 100
P = 63
Q1 = 3*P  # 2**(Q1//3) >= 2**P, s.t. R1, R2, R3 factors would be excluded in the first response
while 2**(Q1//5) <= R * 2**(Q1//6):
    Q1 +=1
assert(R * 2**(Q1//4) < 2**P)
Q2 = 1
while 2**(Q2//2) <= R * 2**(Q2//3):
    Q2 +=1
assert(R * 2**(Q2//1) < 2**P)
T, W = map(int, raw_input().strip().split())
for case in xrange(T):
    draupnir()
