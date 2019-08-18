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
    if start == len(x)-1-start+1:  # terminated statement of even length
        return carry == right_carry
    if start == len(x)-1-start:  # terminated statement of odd length
        for i in xrange(10):
            if start == 0 and i == 0:
                continue
            target = s[len(x)-1-start] + 10*carry - right_carry
            j = target-i
            if not (0 <= j <= 9):
                continue
            if start == 0 and j == 0:
                continue
            x[start], x[-1-start] = i, i
            y[start], y[-1-start] = j, j
            return True
        return False
    
    for i in xrange(10):
        for new_carry in xrange(2):
            if start == 0 and i == 0:
                continue
            target = s[len(x)-1-start] + 10*carry - new_carry
            j = target-i
            if not (0 <= j <= 9):
                continue
            if start == 0 and j == 0:
                continue
            if s[start] != (i+j+right_carry)%10:
                continue
            x[start], x[-1-start] = i, i
            y[start], y[-1-start] = j, j
            if find_pair_with_same_length(s, x, y, start+1, new_carry, (i+j+right_carry)//10):
                return True
            y[start], y[-1-start] = None, None
            x[start], x[-1-start] = None, None

def get_overhang(s, start, overhang):
    return int("".join(map(str, s[-(start+overhang):-start])))

def find_pair_with_hangover_length(s, x, y, start, carry, right_carry):
    return False
    overhang = len(x)-len(y)
    get_overhang(s, start, overhang)
    return False

def find_pair(S, i, j, carry):
    s = map(int, list(str(S)))
    s.reverse()
    x, y = [None]*i, [None]*j
    if i == j:
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
            for j in xrange(1, i+1):
                result = find_pair(s, i, j, carry)
                if result is not None:
                    # if (S != p + result[0] + result[1]):
                    #     print S, "!=", p + result[0] + result[1], "(", p, result[0], result[1], ")", carry
                    assert(S == p + result[0] + result[1])
                    for i in result:
                        assert(0 < i <= S)
                    if p == 0:
                        return "%d %d" % (result[0], result[1])
                    return "%d %d %d" % (p, result[0], result[1])
    #assert(False)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, wont_sum_must_now())