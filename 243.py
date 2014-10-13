from common import mymath
primes = mymath.PrimeLst(10 ** 3)


def seq():
    """
    >>> a = seq(); [a.next() for i in xrange(20)]
    [2, 4, 6, 12, 18, 24, 30, 60, 90, 120, 150, 180, 210, 420, 630, 840, 1050, 1260, 1470, 1680]
    """
    p0, v, d = 2, 2, 2
    yield v
    for p in primes[1:]:
        for i in xrange(p - 1):
            v += d
            yield v
        p0, d = p, v


def fastSeq():
    """
    >>> a = fastSeq(); [a.next() for i in xrange(10)]
    [2, 6, 30, 210, 2310, 30030, 510510, 9699690, 223092870, 6469693230]
    """
    v = 1
    for p in primes:
        v *= p
        yield v


def prod(lst):
    import operator
    return reduce(operator.mul, lst, 1)


def Resilient(n):
    """
    12 -> 1 5 7 11
       -> 2 3 4 6 8 9 10
       -> {2 4 6 8 10 12} + {3 6 9 12} - {6 12}
    1 - {[1/2 + 1/3] - 1/6}
    4/11 = 0.36..
    >>> Resilient(12)
    0.36363636363636365
    """
    from itertools import combinations
    seq = mymath.factorLst(n)
    seq = [k for k, v in seq]
    r, fac = n, 1
    for i in xrange(1, len(seq) + 1):
        lst = combinations(seq, i)
        fac *= -1
        lst = [prod(v) for v in lst]
        lst = [n / v for v in lst]
        s = sum(lst)
        r += fac * s
    return r / (n - 1.0)


if __name__ == "__main__":
    thres = 15499 / 94744.0
    v = 2
    origin_thres = Resilient(v)
    from itertools import count
    arr = seq()
    while 1:
        i = arr.next()
        ratio = Resilient(i)
        print i, ratio, origin_thres - ratio, ratio - thres
        origin_thres = ratio
        if ratio < thres:
            print i
            break
