# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1A - Problem B. Golf Gophers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05
#
# Time:  O(B * N + BlogM))
# Space: O(B)
#

import sys
import itertools

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# https://rosettacode.org/wiki/Chinese_remainder_theorem
def chinese_remainder(n, a):  # Time: O(BlogM), len(n) = B, PI(n) = M
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in itertools.izip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

B = 18
def golf_gophers(N, M):
    modulis, residues = [], []
    cnt = 1
    for i in reversed([5, 7, 9, 11, 13, 16, 17]):
        print " ".join(map(str, [i]*B))
        sys.stdout.flush()
        modulis.append(i)
        residues.append(sum(map(int, raw_input().strip().split())) % i)
        cnt *= i
        if i > M:
            break

    # these modulis work in chinese remainder theorem (each one is prime to the other)
    print chinese_remainder(modulis, residues)
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

T, N, M = map(int, raw_input().strip().split())
for case in xrange(T):
    golf_gophers(N, M)
