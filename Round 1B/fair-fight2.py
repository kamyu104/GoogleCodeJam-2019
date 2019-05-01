# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem C. Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
#
# Time:  O(NlogN)
# Space: O(NlogN)
#

import collections
import itertools

class RangeQuery(object):
    def __init__(self, items, fn):
        self.__rq = rq = {(i, 0): item for i, item in enumerate(items)}
        self.__fn = fn
        self.__pow = [1]
        self.__bit_length = []
        n = len(items)
        for i in xrange(1, n.bit_length()):
            self.__pow.append(self.__pow[-1] * 2)
        count = 1
        for i in xrange(1, n.bit_length()+1):          
            self.__bit_length.extend([i]*min(count, n-len(self.__bit_length)))
            count *= 2
        for step, i in itertools.product(xrange(1, n.bit_length()), xrange(n)):  # O(NlogN)
            j = i + self.__pow[step-1]
            if j < n:
                rq[i, step] = fn(rq[i, step-1], rq[j, step-1])
            else:
                rq[i, step] = rq[i, step-1]

    def query(self, start, stop):  # O(1)
        j = self.__bit_length[stop-start-1]-1
        x = self.__rq[start, j]
        y = self.__rq[stop - self.__pow[j], j]
        return self.__fn(x, y)

def lower_bound(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if check(mid):
            right = mid-1
        else:
            left = mid+1
    return left

def upper_bound(left, right, check):
    while left <= right:
        mid = left + (right-left)//2
        if not check(mid):
            right = mid-1
        else:
            left = mid+1
    return left

def fair_fight():
    N, K = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())
    C_RMQ, D_RMQ = RangeQuery(C, max), RangeQuery(D, max)
    result, next_to_last_seen = 0, collections.defaultdict(int)
    for i, Ci in enumerate(C):
        L_good = lower_bound(next_to_last_seen[Ci], i,
                             lambda x: C_RMQ.query(x, i+1) == Ci and D_RMQ.query(x, i+1)-Ci <= K)
        R_good = upper_bound(i, N-1,
                             lambda x: C_RMQ.query(i, x+1) == Ci and D_RMQ.query(i, x+1)-Ci <= K)-1
        L_bad = lower_bound(L_good, i,
                            lambda x: C_RMQ.query(x, i+1) == Ci and D_RMQ.query(x, i+1)-Ci <= -K-1)
        R_bad = upper_bound(i, R_good,
                            lambda x: C_RMQ.query(i, x+1) == Ci and D_RMQ.query(i, x+1)-Ci <= -K-1)-1
        result += (i-L_good+1)*(R_good-i+1)-(i-L_bad+1)*(R_bad-i+1)
        next_to_last_seen[Ci] = i+1  # to avoid duplicated count
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fair_fight())
