import itertools

pl = []


def compsite():
    p = 2
    global pl
    pl = [p]
    for i in itertools.count(p + 1):
        isPrime = True
        for p0 in pl:
            if i % p0 == 0:
                isPrime = False
                break
            if p0 * p0 > i:
                break
        if isPrime:
            pl.append(i)
        else:
            yield i

squarelst = set({1})
msquare = 1


def incSquareLst(squarelst, ms, n):
    if ms ** 2 > n:
        return squarelst, ms
    for i in itertools.count(ms):
        v = i ** 2
        squarelst.add(v)
        if v > n:
            break
    return squarelst, i


def isSquare(n):
    global msquare, squarelst
    squarelst, msquare = incSquareLst(squarelst, msquare, n)
    return n in squarelst


def isConj(n):
    for p in pl:
        if n < p:
            return False
        d = n - p
        if d % 2 == 0 and isSquare(d / 2):
            return True

comp = compsite()
while 1:
    n = comp.next()
    if n % 2 == 0:
        continue
    if not isConj(n):
        print n
        break
