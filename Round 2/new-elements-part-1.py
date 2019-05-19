# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 2 - Problem A. New Elements: Part 1
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146183
#
# Time:  O(N^2)
# Space: O(N^2)
#

from fractions import Fraction

def new_elements_part_1():
    N = input()
    molecules = []
    for _ in xrange(N):
        molecules.append(map(int, raw_input().strip().split()))

    fractions_set = set()
    for i in xrange(N-1):
        (Ca, Ja) = molecules[i]
        for j in xrange(i+1, N):
            (Cb, Jb) = molecules[j]
            # let R = wJ/wC
            # => Ca * wC + Ja * R * wC < Cb * wC + Jb * R * wC
            # => Ca + Ja * R < Cb + Jb * R
            # => (Ca-Cb) < (Jb-Ja) * R
            # for each pair if 0 < (Ca-Cb)/(Jb-Ja) < inf
            #     if we let R = (Ca-Cb)/(Jb-Ja),
            #     it will decide a unique ordering
            if Ca < Cb and Ja > Jb:
                fractions_set.add(Fraction(Ca-Cb, Jb-Ja))
    return len(fractions_set)+1

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, new_elements_part_1())
