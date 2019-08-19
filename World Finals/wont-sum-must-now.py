# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem C. Won't sum? Must now
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77e
#
# Time:  O(2^(D/2) * D), D is the number of digits of S
# Space: O(D)
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
    if len(x)-start*2 <= 0:
        return left_carry == right_carry
    for i in xrange(10):
        for new_left_carry in xrange(2):
            if start == 0 and i == 0:  # leading digit can't be 0
                continue
            target = s[len(x)-1-start] + left_carry*10 - new_left_carry
            j = target-i
            if not (0 <= j < 10):
                continue
            if start == 0 and j == 0: # leading digit can't be 0
                continue
            if s[start] != (i+j+right_carry)%10:
                continue
            x[start], x[-1-start] = i, i
            y[start], y[-1-start] = j, j
            new_right_carry = (i+j+right_carry)//10
            if len(x)-start*2 == 1:
                new_right_carry = right_carry
            if find_pair_with_same_length(s, x, y, start+1, new_left_carry, new_right_carry):
                return True
            y[start], y[-1-start] = None, None
            x[start], x[-1-start] = None, None

def find_pair_with_hangover_length(s, x, y, start, left_carry, right_carry, last_left_y):
    def apply(x, o, start):
        for i in xrange(len(o)):
            x[start+i] = o[i]
        for i in xrange(len(o)):
            if x[-1-(start+i)] is None:
                x[-1-(start+i)] = o[i]
            elif x[-1-(start+i)] != o[i]:
                return False
        return True

    def rollback(x, o, start):
        for i in xrange(len(o)):
            x[start+i], x[-1-(start+i)] = None, None

    if len(x)-start*2 <= 0:
        return left_carry == right_carry
    overhang = min(len(x)-2*start, len(x)-len(y))
    for new_left_carry in xrange(2):
        # find left x to be updated
        left_x = int("".join(map(str, s[len(x)-1-(start+overhang-1):len(x)-start][::-1]))) + \
                                      left_carry*(10**overhang) - new_left_carry - last_left_y
        if not (0 <= left_x < 10**overhang):
            continue
        left_X = map(int, list(str(left_x)))
        left_X = [0]*(overhang-len(left_X)) + left_X  # zero-padding
        if start == 0 and left_X[0] == 0:  # leading digit can't be 0
            continue
        if not apply(x, left_X, start):
            rollback(x, left_X, start)
            continue
        right_Y = []
        new_right_carry = right_carry  # pass current right carry if y is not updated
        new_last_left_y = 0
        if len(y)-start*2 > 0:  # if y needs update
            # find right y to be updated
            right_y_len = min(len(y)-start*2, overhang)
            right_s = int("".join(map(str, s[start:start+right_y_len][::-1])))
            right_x = int("".join(map(str, left_X[:right_y_len][::-1])))
            new_right_carry, right_y = divmod(right_s-right_x-right_carry, 10**right_y_len)
            new_right_carry = abs(new_right_carry)
            right_Y = map(int, list(str(right_y)[::-1]))
            right_Y = right_Y + [0]*(right_y_len-len(right_Y))
            if start == 0 and right_Y[0] == 0:  # leading digit can't be 0
                rollback(x, left_X, start)
                continue
            if not apply(y, right_Y, start):
                rollback(y, right_Y, start)
                rollback(x, left_X, start)
                continue
            # find left y to be updated
            if len(y)-start*2 > overhang:
                new_last_left_y = int("".join(map(str, right_Y[:(len(y)-start*2)-overhang])))
        if find_pair_with_hangover_length(s, x, y, start+overhang,
                                          new_left_carry, new_right_carry, new_last_left_y):
            return True
        rollback(y, right_Y, start)
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
                    if P == 0:
                        return "%d %d" % (result[0], result[1])
                    return "%d %d %d" % (P, result[0], result[1])
    assert(False)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, wont_sum_must_now())
