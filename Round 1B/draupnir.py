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
    Q = 200
    assert(2**(Q//5) > 100 * 2**(Q//6))
    print Q
    sys.stdout.flush()
    N = input()
    R6 = (N % 2**(Q//5)) // 2**(Q//6)
    N -= R6 * 2**(Q//6)
    N %= 2**63
    R5 = (N % 2**(Q//4)) // 2**(Q//5)
    N -= R5 * 2**(Q//5)
    N %= 2**63
    R4 = N // 2**(Q//4)

    Q = 40
    assert(2**(Q//2) > 100 * 2**(Q//3))
    print Q
    sys.stdout.flush()
    N = input()
    N -= R4 * 2**(Q//4) + R5 * 2**(Q//5) + R6 * 2**(Q//6)
    N %= 2**63
    R3 = (N % 2**(Q//2)) // 2**(Q//3)
    N -= R3 * 2**(Q//3)
    N %= 2**63
    R2 = (N % 2**(Q//1)) // 2**(Q//2)
    N -= R2 * 2**(Q//2)
    N %= 2**63
    R1 = N // 2**(Q//1)

    print R1, R2, R3, R4, R5, R6
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

T, W = map(int, raw_input().strip().split())
for case in xrange(T):
    draupnir()
