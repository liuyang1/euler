# not good
# for 10^6, need to run 13.66 seconds
from common import mymath


thresh = 10 ** 7
primelst = mymath.PrimeLst(thresh)


def cDvisor(n):
    """
    >>> cDvisor(14)
    4
    """
    import operator
    factors = mymath.factorLst(n, primelst)
    l = [i + 1 for f, i in factors]
    return reduce(operator.mul, l, 1)


if __name__ == "__main__":
    lastcnt = 1
    r = 0
    for i in xrange(2, 10 ** 7):
        cnt = cDvisor(i)
        if lastcnt == cnt:
            r += 1
        lastcnt = cnt
    print "ret: ", r
