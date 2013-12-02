from common.mymath import *
import operator

n = 1000*100
Plst = PrimeLst(n)

def factorLst(n):
    lst = []
    for i in Plst:
        if n == 1:
            break
        if n%i==0:
            cnt = 0
            while n%i==0:
                cnt += 1
                n = n/i
            item = (i,cnt)
            lst.append(item)
    return lst


def getFactorNum(flst):
    flst = [freq+1 for prime,freq in flst]
    return reduce(operator.mul,flst,1)


maxnum = 6
for i in xrange(2,100000):
    n = i*(i+1)/2
    flst = factorLst(n)
    num = getFactorNum(flst)
    if num>maxnum:
        print n,num
        print flst
        maxnum = num
        if maxnum>500:
            break
