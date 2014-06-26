import itertools


def primes():
    p = 2
    pl = [p]
    yield p
    for i in itertools.count(p + 1):
        isPrime = True
        for p0 in pl:
            if i % p0 == 0: 
                isPrime = False
                break
            if p0 * p0 > i:
                break
        if isPrime:
            yield i
            pl.append(i)


def tranc(n):
    lst, r = [], 1
    while 1:
        r *= 10
        a, b = n / r, n % r
        if n < r:
            break
        lst.append(n / r)
        lst.append(n % r)
    return lst

import common.mymath

Primes = common.mymath.PrimeLst(10 ** 5)
def isTrancPrime(n):
    l = tranc(n)
    return all([i in Primes for i in l])

s, c = 0, 0
pg = primes()
print "ok"
while 1:
    p = pg.next()
    if isTrancPrime(p):
        c += 1
        s += p
        print p, c
        if c == 11 + 4:
            break
print s
