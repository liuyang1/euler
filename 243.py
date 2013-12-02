from common import mymath


def isResilient(n, thres):
    thresI = n * thres
    cnt = 1
    for i in xrange(2, n):
        if mymath.bingcd(n, i) == 1:
            cnt += 1
            if cnt > thresI:
                print n, thresI, cnt
                return False
    return True

thres = 15499 / 94744.0
from itertools import count
for i in count(4, 6):
    if isResilient(i, thres):
        print i
        break
