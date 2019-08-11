# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem A. Board Meeting
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77c
#
# Time:  O(NlogM)
# Space: O(N)
#

from sys import stdout

def print_line(s):
    print s
    stdout.flush()

def read_line():
    s = raw_input()
    if s == "ERROR":
        exit()
    return s

def query_diff(u, v):
    assert(u%2 == v%2)
    print_line("%d %d" % ((u+v)//2, (u-v)//2))
    return int(read_line())*2  # diff_in_U_V = 2 * diff_in_X_Y

def query_U(N, u, swap=False):
    v = 2*M + u%2
    extra_diff = N if u%2 else 0  # there will be extra diff if v has been adjusted for query
    if swap:
        u, v = v, u
    return query_diff(u, v) - extra_diff  # minus extra diff due to adjustment

def board_meeting():
    N = (query_diff(2*M+1, 2*M+1) - query_diff(2*M, 2*M)) // 2
    U, V = [], []  # u = x + y, v = x - y
    for swap, axis in enumerate([U, V]):
        for i in xrange(N):
            left, right = -2*M, 2*M
            while left <= right:
                mid = left + (right-left)//2
                if query_U(N, mid+1, swap) - query_U(N, mid, swap) > -N + i*2:  # if diff is greater than expected one
                    right = mid-1
                else:
                    left = mid+1
            axis.append(left)
    
    print_line("READY")
    while True:
        s = read_line()
        if s == "DONE":
            break
        x, y = map(int, s.strip().split())
        result = 0
        for i in xrange(N):
            result += abs((x+y) - U[i]) + abs((x-y) - V[i])
        result //= 2  # diff_in_X_Y = diff_in_U_V / 2
        print_line(result)

T, MAX_N, M, R = map(int, raw_input().strip().split())
assert(2 + 2 * MAX_N * M.bit_length() * 2 <= R)
for case in xrange(T):
    board_meeting()
