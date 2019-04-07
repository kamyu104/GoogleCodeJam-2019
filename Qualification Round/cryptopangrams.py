# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem C. Cryptopangrams
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#
# Time:  O(LlogN)
# Space: O(1)
#

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def cryptopangrams():
    N, L = map(int, raw_input().strip().split())
    MSG = map(int, raw_input().strip().split())

    primes = set()
    for i in xrange(L-1):
        if MSG[i] == MSG[i+1]:
            continue
        p = gcd(MSG[i], MSG[i+1])
        primes.add(p)
        primes.add(MSG[i]//p)
        primes.add(MSG[i+1]//p)
        if len(primes) == 26:
            break

    lookup = {}
    sorted_primes = sorted(primes)
    for i, p in enumerate(sorted_primes):
        lookup[p] = chr(ord('A')+i)

    for p in sorted_primes:
        result = [lookup[p]]
        for i in xrange(L):
            if MSG[i] % p != 0:
                break
            p = MSG[i]//p
            result.append(lookup[p])
        else:
            return "".join(result)
    return ""  # never reach

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cryptopangrams())
