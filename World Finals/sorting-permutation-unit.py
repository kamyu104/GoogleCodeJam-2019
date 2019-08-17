# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem B. Sorting Permutation Unit
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c77d
#
# Time:  O(K * N^2), each array costs 1.5N + 4N + N = 8.5N operations
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
    seq.extend(ROTATIONS[k])  # split k rotations into at most 4 permutations

def swap_and_add_seq(nums, seq):  # at most 1.5N swaps
    nums[-1], nums[-2] = nums[-2], nums[-1]
    seq.append(1)

def sorting_permutation_unit():
    P, S, K, N = map(int, raw_input().strip().split())

    perms = []
    perms.append(range(1, N+1))
    perms[-1][-1], perms[-1][-2] = perms[-1][-2], perms[-1][-1]
    for r in ROTATE_BY:
        if r > N-2:
            break
        perms.append(range(1, N+1))
        rotate(perms[-1], r, len(perms[-1])-1)

    result = [""]
    result.append(str(len(perms)))
    for perm in perms:
        result.append(" ".join(map(str, perm)))

    for _ in xrange(K):
        A = normalize(map(int, raw_input().strip().split()))
        seq = [0]
        shift = [0]
        while True:
            # rotate the first N-1 ones into the correct positions and swap(N-1, N)
            # until Nth position becomes the largest one,
            # at most 4N operations
            while A[-1] != len(A)-1:
                rotate_and_add_seq(A, (len(A)-2) - (shift[0]+A[-1])%(len(A)-1), seq, shift)
                swap_and_add_seq(A, seq)
            # find the nearest incorrect relative position from the last position
            for nearest_pos in reversed(xrange(len(A)-1)):
                if nearest_pos != (shift[0]+A[nearest_pos])%(len(A)-1):
                    break
            else:
                break
            # rotate the nearest incorrect one to (N-1)th position and swap(N-1, N),
            # at most N operations due to choosing the nearest incorrect one to rotate
            # which makes one full cycle rotatation in total
            rotate_and_add_seq(A, (len(A)-2) - nearest_pos, seq, shift)
            swap_and_add_seq(A, seq)
        # do the final rotations to put them in the correct absolute positions
        rotate_and_add_seq(A, (len(A)-2) - A.index(len(A)-2), seq, shift)
        seq[0] = len(seq)-1
        result.append(" ".join(map(str, seq)))
    return "\n".join(result)

ROTATE_BY = [1, 3, 12, 20]
ROTATIONS = []
MAX_N = 50
dp = [None for _ in xrange(len(ROTATE_BY)*ROTATE_BY[-1]+1)]
dp[0] = []
for i in xrange(1, len(dp)):
    for j in xrange(len(ROTATE_BY)):
        if i-ROTATE_BY[j] < 0 or dp[i-ROTATE_BY[j]] is None:
            continue
        if dp[i] is None or len(dp[i-ROTATE_BY[j]])+1 < len(dp[i]):
            dp[i] = list(dp[i-ROTATE_BY[j]])
            dp[i].append(j+2)  # 1-based index and index 1 reserved for swap permutation
for k in xrange(MAX_N-1):
    ROTATIONS.append(dp[k])
    count = len(ROTATIONS[-1])
    for i in xrange(k+MAX_N-1, len(dp), MAX_N-1):
        if len(dp[i]) < len(ROTATIONS[-1]):
            ROTATIONS[-1] = dp[i]
            count = len(ROTATIONS[-1])
    assert(count <= 4)  # each rotations could be represented as at most 4 permutations
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, sorting_permutation_unit())
