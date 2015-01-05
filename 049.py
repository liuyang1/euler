from common import mymath
import itertools

primes = mymath.PrimeLst(10 ** 4)
primes = [p for p in primes if p > 10 ** 3]

for i0 in xrange(len(primes)):
    p0 = primes[i0]
    d0 = mymath.digit(p0)
    if 0 in d0:
        continue
    for i1 in xrange(i0 + 1, len(primes)):
        p1 = primes[i1]
        p2 = p1 - p0 + p1
        if p2 > 10 ** 4 or p2 not in primes:
            continue
        d1 = mymath.digit(p1)
        # simply check set, not accurate
        if set(d0) != set(d1):
            continue
        d2 = mymath.digit(p2)
        if set(d1) != set(d2):
            continue
        print p0, p1, p2
        break
