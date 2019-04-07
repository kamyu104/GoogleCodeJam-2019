# Time:  O(n)
# Space: O(1)

def you_can_go_your_own_way():
    N = input()
    P = list(raw_input().strip().split()[0])
    result = []
    for move in P:
        if move == 'E':
            result.append('S')
        else:
            result.append('E')
    return "".join(result)

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, you_can_go_your_own_way())
