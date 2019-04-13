# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1A - Problem B. Golf Gophers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a
#
# Time:  O(B * N + BlogM)
# Space: O(B)
#

import sys
import itertools

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
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

def golf_gophers(N, M):
    modulis, residues = [], []
    prod = 1
    for i in reversed(MODULIS):
        print " ".join(map(str, [i]*B))
        sys.stdout.flush()
        modulis.append(i)
        residues.append(sum(map(int, raw_input().strip().split())) % i)
        prod *= i
        if prod >= M:
            break

    # these modulis work in chinese remainder theorem (each one is prime to the others)
    result = chinese_remainder(modulis, residues)
    if result == 0:
        result = prod
    print result
    sys.stdout.flush()
    verdict = input()
    if verdict == -1:  # error
        exit()

def getPrimes(n):
    primes = []
    if n < 2:
        return []

    primes.append(2)
    is_prime = [True] * n
    for i in xrange(3, n+1, 2):
        if not is_prime[i-1]:
            continue
        primes.append(i)
        for j in xrange(i*i, n+1, 2*i):
            is_prime[j-1] = False
    return primes

B = 18
primes = getPrimes(B)
MODULIS = []
for i in xrange(len(primes)): # Time:  O(BlogB)
    moduli = 1
    while moduli * primes[i] <= B:
        moduli *= primes[i]
    MODULIS.append(moduli)
MODULIS.sort()  # [5, 7, 9, 11, 13, 16, 17]

T, N, M = map(int, raw_input().strip().split())
for case in xrange(T):
    golf_gophers(N, M)
