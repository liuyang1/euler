from common.mymath import *

lst = PrimeLst(5*1000)

print "begin to check consecutive prime sum"

for i in range(500,1000):
    print "check %d consecutive prime" % (i)
    for j in range(len(lst)-i):
        l = lst[j:j+i]
        s = sum(l)
        if s>1*1000*1000:
            break
        if isPrime(s):
            print l
            print "len: ",len(l)
            print s
