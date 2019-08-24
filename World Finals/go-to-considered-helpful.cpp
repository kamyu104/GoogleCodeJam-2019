// Copyright (c) 2019 kamyu. All rights reserved.

/*
 * Google Code Jam 2019 World Finals - Problem F. Go To Considered Helpful
 * https:#codingcompetitions.withgoogle.com/codejam/round/0000000000051708/000000000016c934
 *
 * Time:  O(N^4), N is max(R, C)
 * Space: O(N^2)
 *
 */

#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <functional>
#include <utility>
#include <tuple>
#include <algorithm>
#include <cassert>

using std::ios_base;
using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::string;
using std::to_string;
using std::queue;
using std::function;
using std::pair;
using std::make_pair;
using std::tie;
using std::max;
using std::min;

const int MAX_R = 100;
const int MAX_C = 100;
const int INF = MAX_R * MAX_C;

// Time: O(N^2)
vector<vector<int>> inline bfs(const vector<vector<char>>& G,
                               const int r, int c,
                               const function<bool(int, int)>& check_fn) {
    const auto& R = G.size(), &C = G[0].size();
    static const vector<pair<int, int>> directions{{0, 1}, {1, 0},
                                                   {0, -1}, {-1, 0}};
    vector<vector<int>> dist(R, vector<int>(C, INF));
    dist[r][c] = 0;
    queue<pair<int, int>> q({{r, c}});
    while (!q.empty()) {
        int r, c;
        tie(r, c) = q.front(); q.pop();
        for (const auto& kvp : directions) {
            const auto& nr = r + kvp.first, &nc = c + kvp.second;
            if (0 <= nr && nr < R && 0 <= nc && nc < C &&
                dist[nr][nc] == INF && check_fn(nr, nc)) {
                dist[nr][nc] = dist[r][c] + 1;
                q.emplace(nr, nc);
            }
        }
    }
    return dist;
}

bool inline check(const vector<vector<char>>& G, int r, int c) {
    const auto& R = G.size(), &C = G[0].size();
    return 0 <= r && r < R &&
           0 <= c && c < C &&
           G[r][c] != '#';
}

string go_to_considered_helpful() {
    int R, C;
    cin >> R >> C;
    vector<vector<char>> G(R, vector<char>(C));
    pair<int, int> M, N;
    for (int r = 0; r < R; ++r) {
        for (int c = 0; c < C; ++c) {
            cin >> G[r][c];
            if (G[r][c] == 'N') {
                N = make_pair(r, c);
            } else if (G[r][c] == 'M') {
                M = make_pair(r, c);
            }
        }
    }
    const auto& P = bfs(G, M.first, M.second,
        [&G](int r, int c) { return G[r][c] != '#'; });
    int result = P[N.first][N.second];
    int cnt = 0;
    for (int dr = -R + 1; dr < R; ++dr) {  // enumerate (dr, dc)
        for (int dc = -C + 1; dc < C; ++dc) {
            if ((dr == 0 && dc == 0) ||
                !check(G, N.first - dr, N.second - dc)) {
                continue;
            }
            vector<vector<vector<bool>>> is_valid(2,
                vector<vector<bool>>(R, vector<bool>(C)));
            for (int r = 0; r < R; ++r) {
                for (int c = 0; c < C; ++c) {
                    is_valid[0][r][c] = check(G, r, c);
                }
            }
            for (int k = 1;
                 check(G, N.first - dr * k, N.second - dc * k);
                 ++k) {  // enumerate K
                // the number of (dr, dc, k) combinations is
                // at most sum(N / max(abs(dr), abs(dc)))
                // for each (dr, dc) = O(N^2)
                assert(++cnt <= 2 * max(R, C) * max(R, C));
                auto& is_valid_for_all_k_loops = is_valid[k % 2];
                auto& is_valid_for_all_k_minus_1_loops = is_valid[(k - 1) % 2];
                for (int r = 0; r < R; ++r) {
                    for (int c = 0; c < C; ++c) {
                        is_valid_for_all_k_loops[r][c] =
                            is_valid_for_all_k_minus_1_loops[r][c] &&
                            check(G, r - dr * k, c - dc * k);
                    }
                }
                const auto& Q1 = bfs(G, N.first, N.second,
                     [&is_valid_for_all_k_loops](int r, int c) {
                         return is_valid_for_all_k_loops[r][c];
                     });
                const auto& Q2 = bfs(G, N.first - dr, N.second - dc,
                     [&is_valid_for_all_k_minus_1_loops](int r, int c) {
                         return is_valid_for_all_k_minus_1_loops[r][c];
                     });
                for (int r = 0; r < R; ++r) {  // enumerate all possible cells B
                    for (int c = 0; c < C; ++c) {
                        if (!check(G, r - dr * k, c - dc * k)) {
                            continue;
                        }
                        // instructions:
                        // M ---P---> B ---Q1---> N ---Q2---> Goto B
                        result = min(result,
                                     P[r - dr * k][c - dc * k] +
                                     Q1[r][c] + Q2[r][c] + 1);
                    }
                }
            }
        }
    }
    return result == INF ? "IMPOSSIBLE" : to_string(result);
}

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << go_to_considered_helpful() << endl;
    }
    return 0;
}
