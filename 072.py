from common import mymath

N = 10 ** 6
primelst = frozenset(mymath.PrimeLst(N + 1))
print "primelst ok"

def factor(a):
    if a in primelst:
        return set([a])
    fac = set()
    for p in primelst:
        if a == 1:
            break
        if a % p == 0:
            fac.add(p)
            while a % p == 0:
                a /= p
    return fac


dct = {}
for n in xrange(2, N + 1):
    if n in primelst:
        dct[n] = set([n])
    else:
        fac = set()
        for p in primelst:
            if n == 1:
                break
            if n % p == 0:
                fac.add(p)
                fac |= dct[n / p]
        dct[n] = fac
    print n, dct[n]

print "factor lst ok"

cnt = 0
for d in range(2, N + 1):
    dd = dct[d]
    cnt += 1
    for n in range(2, d):
        ud =  dd & dct[n]
        if len(ud) == 0:
            cnt += 1
print cnt
