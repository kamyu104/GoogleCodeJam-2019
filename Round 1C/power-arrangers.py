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
    total = R_FAC
    Q = range(1, (total-1)*R, R)
    for i in reversed(xrange(2, R+1)):
        total /= i
        if total > 1:
            lookup = collections.defaultdict(list)
            for q in Q:
                print q
                sys.stdout.flush()
                lookup[raw_input()].append(q+1)   
                cnt += 1         
            for k, v in lookup.iteritems():
                if len(v) != total:
                    result.append(k)
                    Q = v
                    break
        else:
            print Q[0]+1
            sys.stdout.flush()
            result.append(raw_input())
            cnt += 1
            result.append((set(chr(ord('A')+i) for i in xrange(R)) - set(result)).pop())
            break
    
    assert(cnt <= F)
    print "".join(result)
    sys.stdout.flush()
    verdict = raw_input()
    if verdict == "N":  # error
        exit()

def factorial(n):
    for i in reversed(xrange(1, n)):
        n *= i
    return n

R = 5
R_FAC = factorial(R)
T, F = map(int, raw_input().strip().split())
for case in xrange(T):
    power_arrangers()
