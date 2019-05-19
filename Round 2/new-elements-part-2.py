# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem C. New Elements: Part 2
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184
#
# Time:  O(N^2)
# Space: O(N^2)
#

from fractions import Fraction

def continued_fraction(a, b, D=0):
    assert(a < b)
    assert(D < 10)
    if b-int(a) > 1:
        return Fraction(int(a)+1, 1)
    if a == int(a):
        return a + Fraction(1, int(1/(b-a))+1)
    return int(a) + 1/continued_fraction(1/(b-int(a)), 1/(a-int(a)), D+1)

def new_elements_part_2():
    N = input()
    molecules = []
    for _ in xrange(N):
        molecules.append(map(int, raw_input().strip().split()))

    lowers, uppers = set(), set()
    for b in xrange(1, N):
        (Cb, Jb) = molecules[b]
        for a in xrange(b):
            (Ca, Ja) = molecules[a]
            if (Ca < Cb and Ja > Jb):
                uppers.add(Fraction(Ca-Cb, Jb-Ja))
            elif (Ca > Cb and Ja < Jb):
                lowers.add(Fraction(Ca-Cb, Jb-Ja))
            elif (Ca >= Cb) and (Ja >= Jb):
                return "IMPOSSIBLE"
    if lowers and uppers:
        lower, upper = max(lowers), min(uppers)
        if lower >= upper:
            return "IMPOSSIBLE"
        cf = continued_fraction(lower, upper)
        return "{} {}".format(cf.denominator, cf.numerator)
    if lowers:
        lower = max(lowers)
        return "{} {}".format(1, int(lower)+1)
    if uppers:
        upper = min(uppers)
        return "{} {}".format(int(1/upper)+1, 1)
    return "1 1"       

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, new_elements_part_2())
