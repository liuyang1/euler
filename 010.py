def isPrime(n):
    r = 2
    while 1:
        if r * r > n:
            return True
        if n % r == 0:
            return False
        r += 1

print sum((i for i in xrange(2, 2000 * 1000) if isPrime(i)))
