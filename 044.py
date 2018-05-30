import sys


def pentagon(n):
    return n * (3 * n - 1) / 2

N = 10 ** 7
PentLst = []
for i in xrange(1, N * 2):
    PentLst.append(pentagon(i))

PentSet = frozenset(PentLst)

print 'start'
for i in range(2, N):
    d = PentLst[i]
    # for j in range(i, N): # this is WRONG
    for j in range(N):
        if PentLst[j + 1] - PentLst[j] > d:
            break
        a = PentLst[j]
        b = a + d
        if b in PentSet:
            print d, a, b, "step 1"
            c = a + b
            if c in PentSet:
                print d, a, b, c, "step 2"
                sys.exit()
            e = d + b
            if e in PentSet:
                print d, a, b, e, "step 2 left"
                sys.exit()

sys.exit()
