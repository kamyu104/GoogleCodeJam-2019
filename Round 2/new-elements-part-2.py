# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem C. New Elements: Part 2
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184
#
# Time:  O(N^2 * log(max(C, J)))
# Space: O(log(max(C, J)))
#

from fractions import Fraction

def find_fraction_with_min_denominator_between(a, b, d=0):
    assert(a < b)
    assert(d < 9)
    if b-int(a) > 1:
        return Fraction(int(a)+1, 1)
    if a-int(a) == 0:
        return int(a) + Fraction(1, int(1/(b-int(a)))+1)
    return int(a) + 1/find_fraction_with_min_denominator_between(1/(b-int(a)), 1/(a-int(a)), d+1)

def new_elements_part_2():
    N = input()
    molecules = []
    for _ in xrange(N):
        molecules.append(map(int, raw_input().strip().split()))

    L, U = Fraction(0, 1), Fraction(MAX_C_J, 1)
    for b in xrange(1, N):
        (Cb, Jb) = molecules[b]
        for a in xrange(b):
            (Ca, Ja) = molecules[a]
            if (Ca < Cb and Ja > Jb):
                U = min(U,  Fraction(Ca-Cb, Jb-Ja))
            elif (Ca > Cb and Ja < Jb):
                L = max(L, Fraction(Ca-Cb, Jb-Ja))
            elif (Ca >= Cb) and (Ja >= Jb):
                return "IMPOSSIBLE"
    if L >= U:
        return "IMPOSSIBLE"

    frac = find_fraction_with_min_denominator_between(L, U)
    return "{} {}".format(frac.denominator, frac.numerator)

MAX_C_J = 10**9
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, new_elements_part_2())
