from common.mymath import *

def quad(n,a,b):
    return n * n + a * n + b
def cntPrime(a,b):
    n = 0
    while 1:
        num = quad(n, a, b)
        if isPrime(num):
            n += 1
        else:
            return n

r = 1000
max = 0
maxcom = (0, 0)
for a in range(-1 * r, r + 1):
    for b in range(-1 * r, r + 1):
        cnt = cntPrime(a,b)
        if cnt > max:
            print a, b, cnt
            max = cnt
            maxcom = (a, b)
print maxcom
print max
print maxcom[0] * maxcom[1]
