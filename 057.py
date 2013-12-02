def sqrt2expan():
    a, b = 3, 2
    while 1:
        yield (a, b)
        a, b = a + 2 * b, a + b


def cntDigit(n):
    cnt = 0
    while n > 0:
        cnt += 1
        n /= 10
    return cnt


sqrt2 = sqrt2expan()
cnt = 0
for i in range(10**3):
    a, b = sqrt2.next()
    if cntDigit(a) > cntDigit(b):
        cnt += 1
print cnt
