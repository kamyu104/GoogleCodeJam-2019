# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem C. Won't sum? Must now
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77e
#
# Time:  left_X(2^(D/2) * D), D is the number of digits of S
# Space: left_X(D)
#

def palindromes(S):
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

def find_pair_with_same_length(s, x, y, start, left_carry, right_carry):
    if start*2 >= len(x):
        return left_carry == right_carry
    for i in xrange(10):
        for new_left_carry in xrange(2):
            if start == 0 and i == 0:  # leading digit can't be 0
                continue
            target = s[len(x)-1-start] + left_carry*10 - new_left_carry
            j = target-i
            if not (0 <= j <= 9):
                continue
            if start == 0 and j == 0: # leading digit can't be 0
                continue
            if s[start] != (i+j+right_carry)%10:
                continue
            x[start], x[-1-start] = i, i
            y[start], y[-1-start] = j, j
            new_right_carry = (i+j+right_carry)//10 if start != len(x)-1-start else right_carry
            if find_pair_with_same_length(s, x, y, start+1, new_left_carry, new_right_carry):
                return True
            y[start], y[-1-start] = None, None
            x[start], x[-1-start] = None, None

def find_pair_with_hangover_length(s, x, y, start, left_carry, right_carry, last_left_y):
    return False
    def apply(x, o, start):
        print x, list(o), start, len(x), len(o)
        for i in xrange(len(o)):
            x[start+i], x[-1-(start+i)] = o[i], o[i]

    def check(x, o, start):
        for j in xrange(len(o)):
            if x[start+j] != x[-1-(start+j)]:
                return False
        return True

    def rollback(x, o, start):
        for i in xrange(len(o)):
            x[start+i], x[-1-(start+i)] = None, None

    def terminate(x, o, start, left_carry, right_carry):
        for i in xrange(len(o)):
            if start+i+1 >= len(x)-1-(start+i):
                return True
        return False

    overhang = len(x)-len(y)
    for new_left_carry in xrange(2):
        # left_x
        left_x = int("".join(map(str, s[len(x)-1-(start+overhang):len(x)-start]))) + \
                 left_carry*(10**overhang) - new_left_carry - last_left_y
        if left_x < 0:
            continue
        left_X = str(left_x)
        if start == 0 and len(left_X) != overhang:  # leading digit can't be 0
            continue
        # right_x
        left_X = "0"*(overhang-len(left_X)) + left_X  # zero-padding
        apply(x, left_X, start)
        if not check(x, left_X, start):
            rollback(x, left_X, start)
            continue
        # right_y
        right_y_len = min((len(y)-1-start)-start-1, overhang)
        right_x = int(left_X[:right_y_len][::-1])
        right_s = int("".join(map(str, s[start:start+right_y_len][::-1])))
        right_y = right_s-right_x
        new_right_carry, right_y = divmod(right_s-right_x, 10**overhang)
        new_right_carry = abs(new_right_carry)
        # left_y
        left_Y = str(right_y)[::-1]
        left_Y = left_Y + "0"*(right_y_len-len(left_Y))
        if start == 0 and left_Y[0] == '0':  # leading digit can't be 0
            continue
        print y, left_Y, start
        apply(y, left_Y, start)
        if not check(y, left_Y, start):
            rollback(y, left_Y, start)
            rollback(x, left_X, start)
            continue
        if terminate(y, left_Y, start, new_left_carry, new_right_carry):
            print s, x, y
            return True
        new_last_left_y = int(left_Y)
        if find_pair_with_hangover_length(s, x, y, start+overhang,
                                          new_left_carry, new_right_carry, new_last_left_y):
            return True
        rollback(y, left_Y, start)
        rollback(x, left_X, start)
    return False

def find_pair(s, i, j, left_carry):
    x, y = [None]*i, [None]*j
    if i == j:
        result = find_pair_with_same_length(s, x, y, 0, left_carry, 0)
    else:
        result = find_pair_with_hangover_length(s, x, y, 0, left_carry, 0, 0)
    if not result:
        return None
    assert(x == x[::-1] and y == y[::-1] and x[0] != 0 and y[0] != 0)
    x.reverse()
    y.reverse()
    return int("".join(map(str, x))), int("".join(map(str, y)))

def wont_sum_must_now():
    S = input()

    s = map(int, list(str(S)))
    if s == s[::-1]:
        return S
    for P in palindromes(S):
        s = map(int, list(str(S-P)))
        s.reverse()
        for i in (len(s), len(s)-1):
            left_carry = 0
            if len(s) > i:
                if s[-1] != 1:
                    continue
                left_carry = 1
            for j in xrange(1, i+1):
                result = find_pair(s, i, j, left_carry)
                if result is not None:
                    assert(S == P + result[0] + result[1])
                    if P == 0:
                        return "%d %d" % (result[0], result[1])
                    return "%d %d %d" % (P, result[0], result[1])
    assert(False)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, wont_sum_must_now())
