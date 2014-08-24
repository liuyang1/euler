from itertools import count
from common import mymath


thres = 10 ** 9
def GouGu():
    for m in count(1):
        for n in xrange(1, m):
            if mymath.gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
                mm = m * m
                nn = n * n
                mn = 2 * m * n
                a = mm - nn
                b = mn
                c = mm + nn
                cc = mm * 2 + mn
                if abs(2 * a - c) == 1 or abs(2 * b - c) == 1:
                    print a, b, c, cc
                    yield cc
                if cc > thres * 2:
                    return

g = GouGu()

lst = list(g)
lst = [i for i in lst if i < thres]
print lst
print sum(lst)
