# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem B. Sort Permutation Unit
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77d
#
# Time:  O(K*N^2)
# Space: O(N)
#

def normalize(nums):
    A = [(num, i) for i, num in enumerate(nums)]
    A.sort()
    lookup = {i:rank for rank, (num, i) in enumerate(A)}
    return map(lambda x: lookup[x], range(len(nums)))

def rotate(nums, k, n):
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end - 1] = nums[end - 1], nums[start]
            start += 1
            end -= 1

    k %= n
    reverse(nums, 0, n)
    reverse(nums, 0, k)
    reverse(nums, k, n)

def rotate_and_add_seq(nums, r, seq, offset):
    offset[0] = (offset[0]+r)%(len(nums)-1)
    rotate(nums, r, len(nums)-1)
    for i in reversed(xrange(len(ROTATES))):
        q, r = divmod(r, ROTATES[i])
        seq.extend([i+2]*q)

def swap_and_add_seq(nums, seq):
    nums[-1], nums[-2] = nums[-2], nums[-1]
    seq.append(1)

def sorting_permutation_unit():
    P, S, K, N = map(int, raw_input().strip().split())
    As = []
    for _ in xrange(K):
        As.append(normalize(map(int, raw_input().strip().split())))

    perms = []
    perms.append(range(1, N+1))
    perms[-1][-1], perms[-1][-2] = perms[-1][-2], perms[-1][-1]
    for r in ROTATES:
        if r > N:
            break
        perms.append(range(1, N+1))
        rotate(perms[-1], r, len(perms[-1])-1)

    result = [""]
    result.append(str(len(perms)))
    for perm in perms:
        result.append(" ".join(map(str, perm)))

    for A in As:
        B = list(A)
        seq = [0]
        offset = [0]
        if A[-1] != len(A)-1:
            rotate_and_add_seq(A, (len(A)-2) - A.index(len(A)-1), seq, offset)
            swap_and_add_seq(A, seq) 
        while True:
            for curr in reversed(xrange(len(A)-1)):
                if curr != (A[curr]+offset[0])%(len(A)-1):
                    break
            else:
                break
            rotate_and_add_seq(A, (len(A)-2) - curr, seq, offset)
            swap_and_add_seq(A, seq)
            while A[-1] != len(A)-1:
                rotate_and_add_seq(A, (len(A)-2) - (A[-1]+offset[0])%(len(A)-1), seq, offset)
                swap_and_add_seq(A, seq)
        rotate_and_add_seq(A, (len(A)-2) - A.index(len(A)-2), seq, offset)
        seq[0] = len(seq)-1

        result.append(" ".join(map(str, seq)))
    return "\n".join(result)

ROTATES = [1, 3, 9, 27]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, sorting_permutation_unit())
