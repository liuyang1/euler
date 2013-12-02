def rev(n):
    v = 0
    while n > 0:
        v = v * 10 + n % 10
        n = n / 10
    return v


oddset = frozenset([1,3,5,7,9])
def isOddDigit(n):
    while n:
        r = n % 10
        if r not in oddset:
            return False
        n = n / 10
    return True


N = 10 ** 9
cnt = 0
for n in xrange(1, N):
    if n % 10 == 0:
        continue
    if isOddDigit(n + rev(n)):
        cnt += 1
print cnt
