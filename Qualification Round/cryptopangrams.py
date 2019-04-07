# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Qualification Round - Problem C. Cryptopangrams 
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b
#
# Time:  O(L + sqrt(N))
# Space: O(L)
#

def primes(number):
    p = 2
    if number % p == 0:
        return p, number // p
    p += 1
    while p*p <= number:
        if number % p == 0:
            return p, number // p
        p += 2
    return None  # never reach

def decrypt(MSG, min_i, start_p, result):
    prime_set = set()

    p, i = start_p, min_i
    while i >= 0:
        if MSG[i] % p != 0:
            return False
        p = MSG[i] // p
        result.append(p)
        prime_set.add(p)
        i -= 1
    result.reverse()

    p, i = start_p, min_i
    p = MSG[i] // p
    while i < len(MSG):
        if MSG[i] % p != 0:
            return False
        p = MSG[i] // p
        result.append(p)
        prime_set.add(p)
        i += 1

    primes = list(prime_set)
    primes.sort()
    lookup = {}
    for i, p in enumerate(primes):
        lookup[p] = chr(ord('A')+i)

    for i in xrange(len(result)):
        result[i] = lookup[result[i]]
    return True

def cryptopangrams():
    N, L = map(int, raw_input().strip().split())
    MSG = map(int, raw_input().strip().split())
    min_i = MSG.index(min(MSG))
    for start_p in primes(MSG[min_i]):
        result = []
        if decrypt(MSG, min_i, start_p, result):
            break
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, cryptopangrams())
