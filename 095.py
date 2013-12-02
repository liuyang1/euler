from math import sqrt


def getSumDivsor(n):
    if n == 1 or n == 0:
        return 0
    cnt = 1
    for i in range(2, int(sqrt(n)) + 1):
        r = n % i
        if r == 0:
            cnt += n / i
            cnt += i
    return cnt


def cntChain(n):
    s = set([n])
    v = n
    while 1:
        v = getSumDivsor(v)
        if v == 0:
            return (0, s)
        if v == n:
            return (len(s), s)
        else:
            s.add(v)

m = 0
for i in range(10 ** 6):
    v = cntChain(i)
    lv = v
    if lv > m:
        m = lv
        print i, lv
    if i % 10 == 0:
        print "skip",i
