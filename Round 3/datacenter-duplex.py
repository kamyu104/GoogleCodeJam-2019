# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 3 - Problem C. Datacenter Duplex
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051707/0000000000158f1c
#
# Time:  O(R * C)
# Space: O(R * C)
#

class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)
        self.count = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.count -= 1

def get_id(i, j, C):
    return i*C + j

def datacenter_duplex():
    R, C = map(int, raw_input().strip().split())
    M = []
    for _ in xrange(R):
        M.append(list(raw_input().strip()))

    union_find = UnionFind(R*C)
    for i in xrange(R):
        for j in xrange(C):
            if i+1 < R and M[i][j] == M[i+1][j]:
                union_find.union_set(get_id(i, j, C), get_id(i+1, j, C))
            if j+1 < C and M[i][j] == M[i][j+1]:
                union_find.union_set(get_id(i, j, C), get_id(i, j+1, C))

    arrangement = [['.' for _ in xrange(C-1)] for _ in xrange(R-1)]
    for i in xrange(R-1):
        for j in xrange(C-1):
            if not (M[i][j] != M[i+1][j] and \
                    M[i][j] != M[i][j+1] and \
                    M[i][j] == M[i+1][j+1]):
                    continue
            if union_find.find_set(get_id(i, j, C)) != union_find.find_set(get_id(i+1, j+1, C)):
                union_find.union_set(union_find.find_set(get_id(i, j, C)),
                                     union_find.find_set(get_id(i+1, j+1, C)))
                arrangement[i][j] = '\\'
            elif union_find.find_set(get_id(i+1, j, C)) != union_find.find_set(get_id(i, j+1, C)):
                union_find.union_set(union_find.find_set(get_id(i+1, j, C)),
                                     union_find.find_set(get_id(i, j+1, C)))
                arrangement[i][j] = '/'

    if union_find.count > 2:
        return "IMPOSSIBLE"

    result = ["POSSIBLE"]
    for row in arrangement:
        result.append("".join(row))
    return "\n".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, datacenter_duplex())
