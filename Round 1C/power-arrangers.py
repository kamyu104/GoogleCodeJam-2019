# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1C - Problem B. Power Arrangers
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134e91
#
# Time:  O(5!-1 + 4!-1 + 3!-1 + 2!-1 = 148) = O(R!)
# Space: O(5!-1 + 4!-1 + 3!-1 + 2!-1 = 148) = O(R!)
#

import sys
import collections

def power_arrangers():
    result, cnt = [], 0
    expected_permutation_cnt = R_FAC
    Q = range(1, (expected_permutation_cnt-1)*R, R)
    for i in reversed(xrange(2, R+1)):
        if len(Q) > 1:
            lookup = collections.defaultdict(list)
            for q in Q:
                print q
                sys.stdout.flush()
                lookup[raw_input()].append(q+1)  # inspect the next letter
                cnt += 1
            expected_permutation_cnt //= len(lookup)
            for k, v in lookup.iteritems():
                if len(v) != expected_permutation_cnt:  # missing letter in current position
                    result.append(k)
                    Q = v
                    break
        else:  # only the last 2 letters remain unknown
            print Q[0]+1  # inspect the rightmost letter, which is the second letter from the right in the missing set
            sys.stdout.flush()
            result.append(raw_input())
            cnt += 1
            result.append((set(chr(ord('A')+i) for i in xrange(R)) - set(result)).pop())

    assert(cnt <= F)
    print "".join(result)
    sys.stdout.flush()
    verdict = raw_input()
    if verdict == "N":  # error
        exit()

def factorial(n):
    result = 1
    for i in reversed(xrange(1, n+1)):
        result *= i
    return result

R = 5
R_FAC = factorial(R)
T, F = map(int, raw_input().strip().split())
for case in xrange(T):
    power_arrangers()
