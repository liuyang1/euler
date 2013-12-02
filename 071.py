from common import mymath

def HCF(a,b):
    return mymath.bingcd(a,b)


N = 10 ** 6
mind = 1
mn, md = 1, 1
TARGET = 3/7.0
for d in xrange(N, 2, -1):
    print mn, md
    n = 3 * d / 7
    if HCF(d, n) == 1:
        v = n / (d + 0.0)
        diff = TARGET - v
        if TARGET == v:
            continue
        if diff < mind: 
            mind = diff
            mn, md = n, d
print mn, md
