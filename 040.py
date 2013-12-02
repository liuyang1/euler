
tlst = []
for i in range(7):
    tlst.append(10**i)

s = '.'
i = 1
while len(s)<=10**6:
    s += str(i)
    i += 1
ans = [ int(s[i]) for i in tlst]
import operator
print reduce(operator.mul,ans,1)

import sys
sys.exit()

def cham():
    n = 1
    while 1:
        l = str(n)
        for i in l:
            yield i
        n += 1

tlst = []
for i in range(7):
    tlst.append(10**i)
ch = cham()
ans = []

import time
t = time.clock()
for i in range(0,10**6):
    v = ch.next()
    ans.append(v)
print "%.3fms" % (1000 * (time.clock() - t))
ans = [ int(ans[i-1]) for i in tlst]
import operator
print reduce(operator.mul,ans,1)
