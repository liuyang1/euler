from common.mymath import *

N = 10**6
plst = PrimeLst(N)


def cntPrime(n):
    cnt = 0
    i = 0
    while 1:
        if n == 1:
            return cnt
        prime = plst[i]
        if n % prime == 0:
           cnt += 1 
           while n % prime == 0:
               n = n / prime
        i += 1

n = 2
flag = 0
DST = 4
while 1:
    n += 1
    print "\r%10d" % (n),
    if cntPrime(n) == DST:
        flag += 1
        if flag == DST:
            print 
            print n - DST + 1
            break
    else:
        flag = 0
