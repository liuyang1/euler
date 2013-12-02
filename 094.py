from common import mymath

thres = 10 ** 4
square = ([i ** 2 for i in range(thres/2)])


def isEquilateralArea(a,b):
    if b % 2 != 0:
        return False
    b2 = b / 2
    s2 = a * a - b2 * b2
    if s2 in square:
        return a + a + b
    else:
        return False

cnt = 0
for i in xrange(3, thres / 3 + 1, 2):
    v = isEquilateralArea(i, i - 1)
    if v != False:
        print i, (i - 1) / 2
        cnt += v
    v = isEquilateralArea(i, i + 1)
    if v != False:
        print i, (i + 1) / 2
        cnt += v
print cnt
