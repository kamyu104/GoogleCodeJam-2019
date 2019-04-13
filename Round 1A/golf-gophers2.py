# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1A - Problem B. Golf Gophers
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a
#
# Time:  O(B * (N + M))
# Space: O(B)
#

import sys

B = 18
def golf_gophers(N, M):
    modulis, residues = [], []
    for i in reversed(xrange(max(2, B-N+1), B+1)):
        print " ".join(map(str, [i]*B))
        sys.stdout.flush()
        modulis.append(i)
        residues.append(sum(map(int, raw_input().strip().split())) % i)

    # these modulis won't work in chinese remainder theorem (because each one is not prime to the others),
    # but residues are still unique if M <= 1113840 in modulis of [18, 17, 16, 15, 14, 13, 12].
    # see golf-gophers2-prove.py
    for m in xrange(1, M+1):
        for i, residue in enumerate(residues):
            if m % modulis[i] != residue:
                break
        else:
            print m
            sys.stdout.flush()
            verdict = input()
            if verdict == -1:  # error
                exit()
            break

T, N, M = map(int, raw_input().strip().split())
for case in xrange(T):
    golf_gophers(N, M)
