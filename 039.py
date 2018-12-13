def gcdbin(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    if a % 2 == 0:
        if b % 2 == 0:
            return 2 * gcdbin(a / 2, b / 2)
        else:
            return gcdbin(a / 2, b)
    else:
        if b % 2 == 0:
            return gcdbin(a, b / 2)
        else:
            return gcdbin(abs(a - b), min(a, b))
from math import sqrt
from sys import exit

Square = [i ** 2 for i in range(1, 1000 + 1)]
Square = frozenset(Square)


def triOne(n):
    m = n + 1
    nn = n ** 2
    mm = m ** 2
    mm1 = mm + 2 * m + 1
    l = []
    while 1:
        ss = nn + mm
        if ss < mm1:
            break
        if ss in Square:
            l.append((n, m, int(sqrt(ss))))
        mm = mm1
        m += 1
        mm1 += 2 * m + 1
    return l


ans = {}
for i in range(333):
    lst = triOne(i)
    for c in lst:
        s = sum(c)
        if s > 10 ** 3:
            continue
        if s in ans.keys():
            ans[s] += 1
        else:
            ans[s] = 1

vm = 4
for k, v in ans.iteritems():
    if v >= vm:
        print k, v
        vm = v
