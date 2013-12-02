from math import sqrt


def getSumSquDiv(n):
    if n == 1:
        return 1
    cnt = 1 + n ** 2
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt += i ** 2
            v = n / i
            if v != i:
                cnt += (n / i) ** 2
    return cnt


Square = frozenset([i ** 2 for i in range(10**3)])

print "prepare"

cnt = 0
for n in range(1,64*10**6):
    v = getSumSquDiv(n)
    if v in Square:
        print n, v
        cnt += n
print "final"
print cnt
