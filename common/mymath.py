#*-* coding=utf-8
import math
import sys


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


def gcd(x, y):
    while 1:
        x, y = y, x % y
        if y == 0:
            return x


def cntDigit(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n /= 10
    return cnt


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
    使用筛法求素数
    """
    lst = range(0, n + 1)
    lst[1] = 0
    thres = int(math.sqrt(n))
    for i in xrange(2, thres + 1):
        if lst[i] == 0:
            continue
        for j in xrange(i + 1, len(lst)):
            if lst[j] != 0 and lst[j] % lst[i] == 0:
                lst[j] = 0
    lst = [i for i in lst if i != 0]
    return lst
