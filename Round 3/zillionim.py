# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 3 - Problem A. Zillionim
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051707/0000000000158f1a
#
# Time:  O(R^3), R is the max number of rounds
# Space: O(R^2)
#
# python interactive_runner.py python testing_tool.py 2 -- python zillionim.py
#

# perfect solution by Sprague–Grundy theorem, although it is less efficient than 2*10^10 strategy 

from sys import stdout
from random import shuffle, seed

def mex(s):  # minimum excludant
    excludant = 0
    while excludant in s:
        excludant += 1
    return excludant

def init_grundy():  # Time: O(R^2)
    grundy = [0]
    for count in xrange(1, R+1):
        s = set()
        for i in xrange(count):
            s.add(grundy[i] ^ grundy[count-1-i])
        for i in xrange(count-1):
            s.add(grundy[i] ^ grundy[count-2-i])
        grundy.append(mex(s))
    return grundy

def find_grundy(segments):  # Time: O(R^2)
    g = 0
    for _, length in segments:
        g ^= grundy[length//L]
    if g:
        for start, length in segments:
            count = length//L
            for i in xrange(count):
                if g ^ grundy[count] ^ grundy[i] ^ grundy[count-1-i] == 0:
                    return start + i*L
            for i in xrange(count-1):
                if g ^ grundy[count] ^ grundy[i] ^ grundy[count-2-i] == 0:
                    l = length%L
                    mid_length = l + (L-l)//2
                    return start + i*L + mid_length
    return segments[0][0]

def insert_segment(segments, p):
    for i in xrange(len(segments)):
        start, length = segments[i]
        if start <= p <= start+length-1:
            segments[i] = start, p-start
            segments.append((p+L, start+length-(p+L)))
            break
    return [(start, length) for start, length in segments if length >= L]

def zillionim():
    segments = [(1, R*L)]
    while True:
        P = input()
        if P == -2 or P == -3:
            break
        if P == -1:
            exit()

        segments = insert_segment(segments, P)
        c = find_grundy(segments)  # Time: O(R^2)
        segments = insert_segment(segments, c)
        print c
        stdout.flush()

R, L = 100, 10**10
grundy = init_grundy()
T, W = map(int, raw_input().strip().split())
for case in xrange(T):
    zillionim()
