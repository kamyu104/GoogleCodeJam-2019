import random

B = 100000
N = 100000
T = 10
print T
for _ in xrange(T):
    n = random.randint(1, N)
    k = random.randint(0, B)
    print n, k
    C, D = [], []
    for _ in xrange(n):
        C.append(random.randint(0, B))
        D.append(random.randint(0, B))
    print " ".join(map(str, C))
    print " ".join(map(str, D))
