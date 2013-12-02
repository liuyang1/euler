from itertools import count
from common import mymath


def GouGu():
    for m in count(1):
        for n in xrange(1, m):
            if mymath.gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
                mm = m * m
                nn = n * n
                mn = 2 * m * n
                pp = mm * 2 + mn
                print mm - nn, mn, mm + nn
                yield pp
            #yield (mm - nn, mn, mm + nn, mm * 2 + mn)

g = GouGu()

thres = 100# * 1000
lst = []
while 1:
    v = g.next()
    lst.append(v)
    if v > thres * 2:
        break
primeGouGu = frozenset([i for i in lst if i <= thres])
print primeGouGu

from sys import exit
exit()
oneGouGu = []
for i in primeGouGu:
    FLAG = True
    for j in primeGouGu:
        if i > j and i % j == 0:
            print i, j
            FLAG = False
            break
    if FLAG == True:
        oneGouGu.append(i)
print oneGouGu
