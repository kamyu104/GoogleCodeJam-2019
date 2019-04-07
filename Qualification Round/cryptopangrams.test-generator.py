import random
import sys

def GetPrimes(n):
    primes = []
    is_prime = [True] * n
    for i in xrange(3, n, 2):
        if not is_prime[i]:
            continue
        primes.append(i)
        for j in xrange(i*i, n, 2*i):
            is_prime[j] = False
    return primes

T = 100
N = 10000
PRIMES = GetPrimes(N+1)

print T
for t in xrange(T):
    TXT = []
    L = random.randint(25, 100)
    random.shuffle(PRIMES)
    primes = PRIMES[:26]
    primes.sort()
    for i in xrange(26):
        TXT.append(i)
    while len(TXT) != L+1:
        TXT.append(random.randint(0, 25))
    random.shuffle(TXT)
    result = []
    p = primes[TXT[0]]
    for i in xrange(1, len(TXT)):
        result.append(p * primes[TXT[i]])
        p = primes[TXT[i]]
    print N, L
    print " ".join(map(str, result))
#   print >> sys.stderr, primes
    print >> sys.stderr, "Case #{}:".format(t+1), "".join(map(lambda x : chr(ord('A')+x), TXT))
