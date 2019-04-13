# Copyright (c) 2019 kamyu. All rights reserved.
#
# Google Code Jam 2019 Round 1A - Problem C. Alien Rhyme
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104e05
#
# Time:  O(T), t is size of trie
# Space: O(T)
#

import collections
import functools

def alien_rhyme_helper(node):
    no_rhyme_count = sum(alien_rhyme_helper(child) for c, child in node.iteritems() if child)
    if "_end" in node:
        no_rhyme_count += 1
    if "_root" not in node and no_rhyme_count >= 2:
        no_rhyme_count -= 2
    return no_rhyme_count

def alien_rhyme():
    N = input()
    Ws = []
    for _ in xrange(N):
        W = list(raw_input())
        W.reverse()
        Ws.append(W)
    
    _trie = lambda: collections.defaultdict(_trie)
    trie = _trie()
    trie.setdefault("_root")
    for W in Ws:
        functools.reduce(dict.__getitem__, W, trie).setdefault("_end")
    return N - alien_rhyme_helper(trie)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, alien_rhyme())
