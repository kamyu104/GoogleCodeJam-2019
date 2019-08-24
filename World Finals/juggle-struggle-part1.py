# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem D. Juggle Struggle: Part 1
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77f
#
# Time:  O(NlogN) on average, pass in PyPy2 but Python2
# Space: O(N)
#

from random import randint, seed

def nth_element(nums, n, compare=lambda a, b: a < b):
    def partition_around_pivot(left, right, pivot_idx, nums, compare):
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in xrange(left, right):
            if compare(nums[i], nums[right]):
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1

        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

    left, right = 0, len(nums) - 1
    while left <= right:
        pivot_idx = randint(left, right)
        new_pivot_idx = partition_around_pivot(left, right, pivot_idx, nums, compare)
        if new_pivot_idx == n:
            return
        elif new_pivot_idx > n:
            right = new_pivot_idx - 1
        else:  # new_pivot_idx < n
            left = new_pivot_idx + 1

def area(p, q, r):
    return (p[0]-r[0])*(q[1]-r[1]) - (p[1]-r[1])*(q[0]-r[0])

def pairing(P, left, right, result):
    assert(len(left) == len(right))
    if not left or not right:
        return
    if len(left) == 1 and len(right) == 1:
        result[left[0]], result[right[0]] = right[0], left[0]
        return
    p, q = P[left[randint(0, len(left)-1)]], P[right[randint(0, len(right)-1)]]
    points = []
    for i in left:
        points.append((area(p, q, P[i]), ~i))
    for i in right:
        points.append((area(p, q, P[i]), i))
    mid = len(points)//2
    nth_element(points, mid)
    left1, right1, left2, right2 = [], [], [], []
    for i in xrange(mid):
        if points[i][1] < 0:
            left1.append(~points[i][1])
        else:
            right2.append(points[i][1])
    for i in xrange(mid, len(points)):
        if points[i][1] < 0:
            left2.append(~points[i][1])
        else:
            right1.append(points[i][1])
    pairing(P, left1, right1, result)
    pairing(P, left2, right2, result)

def juggle_struggle_part1():
    N = input()
    P = [None]*(2*N)
    for i in xrange(len(P)):
        P[i] = map(int, raw_input().strip().split())

    bottom_left = P.index(min(P))
    point_idx = [i for i in xrange(len(P)) if i != bottom_left]
    mid = len(point_idx)//2
    nth_element(point_idx, mid, lambda a, b: area(P[a], P[b], P[bottom_left]) < 0)
    mid_idx = point_idx[mid]
    left, right = point_idx[:mid], point_idx[mid+1:]
    result = [None]*(2*N)
    result[bottom_left], result[mid_idx] = mid_idx, bottom_left
    pairing(P, left, right, result)
    return " ".join(map(str, map(lambda x: x+1, result)))

seed(0)
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, juggle_struggle_part1())
