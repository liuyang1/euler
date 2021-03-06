# *-* coding=utf-8
import math


def bingcd(a, b):
    if a == 0 and b == 0:
        return 0
    prod = 1
    while 1:
        if b == 0:
            return prod * a
        while a % 2 == 0 and b % 2 == 0:
            prod *= 2
            a, b = a / 2, b / 2
        while a % 2 == 0:
            a /= 2
        while b % 2 == 0:
            b /= 2
        a, b = b, a % b


def factorLst(n, Plst=None):
    """
    >>> factorLst(12)
    [(2, 2), (3, 1)]
    >>> factorLst(97)
    [(97, 1)]
    >>> factorLst(14)
    [(2, 1), (7, 1)]
    """
    if Plst is None:
        Plst = PrimeLst(10**6)
    lst = []
    for i in Plst:
        if n == 1:
            break
        # this to skip scan all prime list
        if n / i < i:
            lst.append((n, 1))
            break
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n = n / i
            item = (i, cnt)
            lst.append(item)
    return lst


def gcd(x, y):
    while 1:
        x, y = y, x % y
        if y == 0:
            return x


def cntDigit(n, base=10):
    """
    >>> cntDigit(1234)
    4
    """
    cnt = 0
    while n > 0:
        cnt += 1
        n /= base
    return cnt


def digit(n, base=10):
    """
    >>> digit(1234)
    [4, 3, 2, 1]
    """
    lst = []
    while n > 0:
        lst.append(n % base)
        n //= base
    return lst


def digitCounter(n, base=10):
    """
    >>> digitCounter(1234)
    Counter({1: 1, 2: 1, 3: 1, 4: 1})
    """
    from collections import Counter
    return Counter(digit(n, base))


def hashDigitCounter(n, base=10):
    """
    >>> hashDigitCounter(1234)
    (0, 1, 1, 1, 1, 0, 0, 0, 0, 0)
    """
    cnt = digitCounter(n, base)
    lst = [0 for i in range(base)]
    for k, v in cnt.items():
        lst[k] = v
    return tuple(lst)


def getSumDigit(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s


def isPrime(n):
    """
    check is Prime,for positive integer.
    使用试除法
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    i = 2
    thres = math.ceil(math.sqrt(n))
    while i <= thres:
        if n % i == 0:
            return False
        i += 1
    return True

import random


def isPrimeMillerRabin(N):
    """
    Miller-Rabin 随机素数检测
    这个算法存在问题,也就是素数大约有50%概率,被检测为合数.
    而合数,则基本不会被错误的识别为素数(概率与检测册数有关)
    """
    s = 0
    t = N - 1
    while t % 2 == 0:
        t /= 2
        s += 1
    d = t
    if s == 0:
        s = 1
    # N - 1 = 2^s * d
    for i in range(49):
        a = random.randint(1, N - 1)
        for r in range(s):
            if pow(a, d) % N != 1 and pow(a, pow(2, r) * d) % N != N - 1:
                return False
    return True


def isPrimeAKS(n):
    if n <= 1:
        return False
    pass


def isPrimeFermat(n):
    for i in range(49):
        a = random.randint(1, n - 1)
        if pow(a, n - 1) % n != 1:
            return False
    return True


def PrimeLst(n):
    """
    ref:
        http://stackoverflow.com/questions/2068372/
        fastest-way-to-list-all-primes-below-n-in-python
    """
    sieve = [True] * (n / 2)
    for i in xrange(3, int(n ** 0.5) + 1, 2):
        if sieve[i / 2]:
            sieve[i * i / 2::i] = [False] * ((n - i * i - 1) / (2 * i) + 1)
    return [2] + [2 * i + 1 for i in xrange(1, n / 2) if sieve[i]]


def myPrime(n):
    sieve = [True] * n
    primes = [2]
    for i in xrange(3, n, 2):
        if sieve[i]:
            primes.append(i)
            for p in primes:
                if i * p > n:
                    break
                sieve[i * p] = False
    return [i for i in xrange(n) if sieve[i] and i % 2 != 0]


def prod(lst):
    import operator
    return reduce(operator.mul, lst, 1)


if __name__ == "__main__":
    pass
    # print sum(PrimeLst(10 ** 7))
    # print sum(myPrime(10 ** 7))
