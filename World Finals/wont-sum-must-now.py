# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem C. Won't sum? Must now
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77e
#
# Time:  O(2^(D/2) * D), D is the number of digits of S
# Space: O(D)
#

def palindromes(S):
    # yield 0
    # return
    # at most 208 times because the smaller palindrome of triples
    # is at most 10801 in this problem
    for p in xrange(10):
        if p > S:
            return
        yield p
        n = 1
    while True:
        for p in xrange(n, 10*n):
            p = int(str(p) + str(p)[::-1])
            if p > S:
                return
            yield p
        for i in xrange(n, 10*n):
            for j in xrange(10):
                p = int(str(i) + str(j) + str(i)[::-1])
                if p > S:
                    return
                yield p
        n *= 10

def find_pair_with_same_length(s, x, y, start, carry, right_carry):
    #print "--"*3, start, carry, right_carry
    if 2 * start >= len(s):
        if len(s)%2:
            return carry == 0
        #print "end", carry, right_carry
        return carry == right_carry
    for i in xrange(10):
        for need_carry in xrange(2):
            if start == 0 and i == 0:
                continue
            target = s[-1-start] + 10*carry - need_carry
            j = target-i
            if not (0 <= j <= 9):
                continue
            if start == 0 and j == 0:
                continue
            #print start, s[start], right_carry, target2, i, j
            if s[start] != (i+j+right_carry)%10:
                # print s, x, y, start, len(s), i, j
                continue
            #print start, "target2", target2, "=", i, "+", j, "+", need_carry, right_carry
            new_carry_from_right = (i+j+right_carry)//10
            #print "carry", new_carry_from_right, right_carry, x, y
            #print "xx", i, j, new_carry_from_right
            x[start], x[-1-start] = i, i
            y[start], y[-1-start] = j, j
            #print start, "target", target, "=", i, "+", j, "+", need_carry, right_carry
            if find_pair_with_same_length(s, x, y, start+1, need_carry, new_carry_from_right):
                return True
            y[start], y[-1-start] = None, None
            x[start], x[-1-start] = None, None

def find_pair_with_hangover_length(s, x, y, start, carry, right_carry):
    #print "--"*3, start, carry, right_carry
    if 2 * start >= len(s):
        if len(s)%2:
            return carry == 0
        #print "end", carry, right_carry
        return carry == right_carry
    for i in xrange(10):
        for need_carry in xrange(2):
            if start == 0 and i == 0:
                continue
            target = s[-1-start] + 10*carry - need_carry
            j = target-i
            if not (0 <= j <= 9):
                continue
            if start == 0 and j == 0:
                continue
            #print start, s[start], right_carry, target2, i, j
            if s[start] != (i+j+right_carry)%10:
                # print s, x, y, start, len(s), i, j
                continue
            #print start, "target2", target2, "=", i, "+", j, "+", need_carry, right_carry
            new_carry_from_right = (i+j+right_carry)//10
            #print "carry", new_carry_from_right, right_carry, x, y
            #print "xx", i, j, new_carry_from_right
            x[start], x[-1-start] = i, i
            y[start], y[-1-start] = j, j
            #print start, "target", target, "=", i, "+", j, "+", need_carry, right_carry
            if find_pair_with_same_length(s, x, y, start+1, need_carry, new_carry_from_right):
                return True
            y[start], y[-1-start] = None, None
            x[start], x[-1-start] = None, None

def find_pair(S, i, j, carry):
    s = map(int, list(str(S)))
    s.reverse()
    if carry:
        s.pop()      
    x, y = [None]*i, [None]*j
    if len(x) == len(y):
        result = find_pair_with_same_length(s, x, y, 0, carry, 0)
    else:
        result = find_pair_with_hangover_length(s, x, y, 0, carry, 0)
    if not result:
        return None
    assert(x == x[::-1] and y == y[::-1] and x[0] != 0 and y[0] != 0)
    x.reverse()
    y.reverse()
    return int("".join(map(str, x))), int("".join(map(str, y)))

def wont_sum_must_now():
    S = input()

    S_str = str(S)
    if S_str == S_str[::-1]:
        return S_str
    for p in palindromes(S):
        s = S-p
        s_str = str(s)
        for i in (len(s_str), len(s_str)-1):
            carry = 0
            if len(s_str) > i:
                if s_str[0] != '1':
                    continue
                carry = 1
            for j in reversed(xrange(1, i+1)):
                result = find_pair(s, i, j, carry)
                if result is not None:
                    # if (S != p + result[0] + result[1]):
                    #     print S, "!=", p + result[0] + result[1], "(", p, result[0], result[1], ")", carry
                    assert(S == p + result[0] + result[1])
                    assert(result[0] != 0 and result[1] != 0)
                    if p == 0:
                        return "%d %d" % (result[0], result[1])
                    return "%d %d %d" % (p, result[0], result[1])
    #assert(False)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, wont_sum_must_now())
