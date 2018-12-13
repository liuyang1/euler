def isPrime(n):
    r = 2
    while 1:
        if r * r > n:
            return True
        if n % r == 0:
            return False
        r += 1

def oldSln():
    print sum((i for i in xrange(2, 2000 * 1000) if isPrime(i)))


def sieve(m):
    for i in xrange(1, m):

