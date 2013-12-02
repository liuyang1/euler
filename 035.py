from common.mymath import *


def circular(n, length):
    return n / 10 + (n % 10) * 10 ** (length - 1)


def getLen(n):
    l = 0
    while n > 0:
        n = n / 10
        l += 1
    return l


def circle(n):
    length = getLen(n)
    s = {n}
    while 1:
        n = circular(n, length)
        if n in s:
            break
        s.add(n)
    return s


N = 10 ** 6
plst = frozenset(PrimeLst(N))

print "preprare"
s = set()
for i in plst:
    if i in s:
        continue
    ci = circle(i)
    if ci.issubset(plst):
        s = s | ci
print len(s)
