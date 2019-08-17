# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem B. Sort Permutation Unit
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77d
#
# Time:  O(K * N^2), each array costs 1.5N + 6N + N = 8.5N operations
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
            nums[start], nums[end-1] = nums[end-1], nums[start]
            start += 1
            end -= 1

    k %= n
    reverse(nums, 0, n)
    reverse(nums, 0, k)
    reverse(nums, k, n)

def rotate_and_add_seq(nums, k, seq, shift):
    assert(k >= 0)  # k should be non-negative rotation count to avoid wrong permutations
    shift[0] = (shift[0]+k)%(len(nums)-1)
    rotate(nums, k, len(nums)-1)
    for i in reversed(xrange(len(ROTATIONS))):  # split k rotations into at most 6 permutations
        q, k = divmod(k, ROTATIONS[i])
        seq.extend([i+2]*q)

def swap_and_add_seq(nums, seq):  # at most 1.5N swaps
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
    for r in ROTATIONS:
        if r > N:
            break
        perms.append(range(1, N+1))
        rotate(perms[-1], r, len(perms[-1])-1)

    result = [""]
    result.append(str(len(perms)))
    for perm in perms:
        result.append(" ".join(map(str, perm)))

    for A in As:
        seq = [0]
        shift = [0]
        while True:
            # rotate the first N-1 ones into the correct positions and swap(N-1, N)
            # until Nth position becomes the largest one,
            # at most 6N operations
            while A[-1] != len(A)-1:
                rotate_and_add_seq(A, (len(A)-2) - (shift[0]+A[-1])%(len(A)-1), seq, shift)
                swap_and_add_seq(A, seq)
            # find the nearest incorrect relative position from the last position
            for curr in reversed(xrange(len(A)-1)):
                if curr != (shift[0]+A[curr])%(len(A)-1):
                    break
            else:
                break
            # rotate the nearest incorrect one to (N-1)th position and swap(N-1, N),
            # at most N operations due to choosing the nearest incorrect one to rotate
            # which makes one full cycle rotatation in total
            rotate_and_add_seq(A, (len(A)-2) - curr, seq, shift)
            swap_and_add_seq(A, seq)
        # do the final rotations to put them in the correct absolute positions
        rotate_and_add_seq(A, (len(A)-2) - A.index(len(A)-2), seq, shift)
        seq[0] = len(seq)-1
        result.append(" ".join(map(str, seq)))
    return "\n".join(result)

ROTATIONS = [1, 3, 9, 27]
MAX_N = 50
for k in xrange(1, MAX_N-1):
    count = 0
    for i in reversed(xrange(len(ROTATIONS))):
        q, k = divmod(k, ROTATIONS[i])
        count += q
    assert(count <= 6)  # each rotations could be represented as at most 6 permutations

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, sorting_permutation_unit())
