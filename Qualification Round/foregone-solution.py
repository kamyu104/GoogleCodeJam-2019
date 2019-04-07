# Time:  O(logn)
# Space: O(1)

def foregone_solution():
    N = list(str(input()))
    A, B = [], []
    for d in N:
        if d == '4':
            A.append('2')
            B.append('2')
        else:
            A.append(d)
            if B: B.append('0')
    if not B:
        B.append('0')
    return "{} {}".format("".join(A), "".join(B))

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, foregone_solution())
