# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1B - Problem C. Fair Fight
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051706/0000000000122838
#
# Time:  O(NlogN)
# Space: O(NlogN)
#

import collections
import math

class RMQ(object):
    def __init__(self, nums):
        n = 1
        while 2**n <= len(nums):
            n += 1
        n -= 1
        self.__dp = [[0 for _ in xrange(n+1)]for _ in xrange(len(nums))]
        for i in xrange(len(nums)):
            self.__dp[i][0] = nums[i]
        j = 1
        while 2**j <= len(nums):
            for i in xrange(len(nums)+1-2**j):
                self.__dp[i][j] = max(self.__dp[i][j-1], self.__dp[i+2**(j-1)][j-1])
            j += 1

    def query(self, i, j):
        k = int(math.log(j-i+1)/math.log(2))
        return max(self.__dp[i][k], self.__dp[j-2**k+1][k])

def binary_search_left(RMQ_C, RMQ_D, left, right, Ci, K):
    i = right
    while left <= right:
        mid = left + (right-left)//2
        if RMQ_C.query(mid, i) == Ci and \
           RMQ_D.query(mid, i)-Ci <= K:
            right = mid-1
        else:
            left = mid+1
    return left

def binary_search_right(RMQ_C, RMQ_D, left, right, Ci, K):
    i = left
    while left <= right:
        mid = left + (right-left)//2
        if not (RMQ_C.query(i, mid) == Ci and \
                RMQ_D.query(i, mid)-Ci <= K):
            right = mid-1
        else:
            left = mid+1
    return left-1

def fair_fight():
    N, K = map(int, raw_input().strip().split())
    C = map(int, raw_input().strip().split())
    D = map(int, raw_input().strip().split())
    RMQ_C, RMQ_D = RMQ(C), RMQ(D)
    result, next_to_last_seen = 0, collections.defaultdict(int)
    for i in xrange(N):
        L_good = binary_search_left(RMQ_C, RMQ_D, next_to_last_seen[C[i]], i, C[i], K)
        R_good = binary_search_right(RMQ_C, RMQ_D, i, N-1, C[i], K)
        L_bad = binary_search_left(RMQ_C, RMQ_D, L_good, i, C[i], -K-1)
        R_bad = binary_search_right(RMQ_C, RMQ_D, i, R_good, C[i], -K-1)
        result += (i-L_good+1)*(R_good-i+1)-(i-L_bad+1)*(R_bad-i+1)
        next_to_last_seen[C[i]] = i+1  # to avoid duplicated count
    return result

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, fair_fight())
