# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 World Finals - Problem F. Go To Considered Helpful
# https:#codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c934
#
# Time:  O(N^4), N is max(R, C), TLE in test set 2 (PyPy2 TLE, too)
# Space: O(N^2)
#

from collections import deque

def bfs(G, r, c, check_fn):  # Time: O(N^2)
    R, C = len(G), len(G[0])
    dist = [[INF for _ in xrange(C)] for _ in xrange(R)]
    dist[r][c] = 0
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for dr, dc in DIRECTIONS:
            nr, nc = r+dr, c+dc
            if 0 <= nr < R and 0 <= nc < C and \
               dist[nr][nc] == INF and check_fn(nr, nc):
                dist[nr][nc] = dist[r][c]+1
                q.append((nr, nc))
    return dist

def check(G, r, c):
    R, C = len(G), len(G[0])
    return  0 <= r < R and 0 <= c < C and G[r][c] != '#'

def go_to_considered_helpful():
    R, C = map(int, raw_input().strip().split())
    G = []
    for r in xrange(R):
        G.append(raw_input().strip())
        for c in xrange(C):
            if G[r][c] == 'M':
                M = (r, c)
            elif  G[r][c] == 'N':
                N = (r, c)
    P = bfs(G, M[0], M[1], lambda r, c: G[r][c] != '#')
    result = P[N[0]][N[1]]
    cnt = 0
    for dr in xrange(-R+1, R):  # enumerate (dr, dc)
         for dc in xrange(-C+1, C):
            if (dr, dc) == (0, 0) or not check(G, N[0]+dr, N[1]+dc):
                continue
            is_valid = [[[check(G, r, c) if k == 0 else False for c in xrange(C)] for r in xrange(R)] \
                          for k in xrange(2)]
            k = 1
            while check(G, N[0]+dr*k, N[1]+dc*k):  # enumerate k
                cnt += 1
                assert(cnt <= 2*max(R, C)**2)  # the number of (dr, dc, k) combinations is
                                               # at most sum(N / max(abs(dr), abs(dc)))
                                               # for each (dr, dc) = O(N^2)
                is_valid_after_k_loops, is_valid_after_k_minus_1_loops = is_valid[k%2], is_valid[(k-1)%2]
                for r in xrange(R):
                    for c in xrange(C):
                        is_valid_after_k_loops[r][c] = is_valid_after_k_minus_1_loops[r][c] and check(G, r+dr*k, c+dc*k)
                Q1 = bfs(G, N[0], N[1], lambda r, c: is_valid_after_k_loops[r][c])
                Q2 = bfs(G, N[0]+dr, N[1]+dc, lambda r, c: is_valid_after_k_minus_1_loops[r][c])
                for r in xrange(R):
                    for c in xrange(C):
                        if not is_valid_after_k_loops[r][c]:
                            continue
                        # instructions : M ---P---> B ---Q1---> N ---Q2---> Goto B
                        result = min(result, P[r+dr*k][c+dc*k] + Q1[r][c] + Q2[r][c] + 1)
                k += 1
    return "IMPOSSIBLE" if result == INF else result

MAX_R, MAX_N = 100, 100
INF = MAX_R*MAX_N
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, go_to_considered_helpful())
