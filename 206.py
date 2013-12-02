N = 10**18
from math import sqrt


def isTarget(n):
    n = n / 100
    rn = 9
    while n:
        r = n % 10
        if r != rn:
            return False
        rn -= 1
        n = n / 100
    if rn == 0:
        return True
    else:
        return False

    
for i in xrange(int(sqrt(N)) / 10 * 10, int(sqrt(N * 2)), 10):
    t = (i / 10) % 10
    if t == 3 or t == 7:
        v = i ** 2
        print i,v
        if isTarget(v):
            print i
            break
