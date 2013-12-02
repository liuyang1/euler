from itertools import count
from common import mymath


def searchN(n):
    cnt = 0
    for i in count(1):
        dn = mymath.cntDigit(i ** n)
        if dn == n:
            cnt += 1
        elif dn > n:
            break
    return cnt


cnt = 0
for i in count(1):
    v = searchN(i)
    if v == 0:
        break
    cnt += v
print cnt
