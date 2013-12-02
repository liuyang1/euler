from common.mymath import *
from math import sqrt
thres = int(sqrt(55*10**6)) + 1
pl = PrimeLst(thres)

from itertools import product

def PrimePower(com):
    return com[0] ** 2 + com[1] ** 3 + com[2]** 4


THRES = 50*10**6
cnt = 0
vset = set()
for i in pl:
    for j in pl:
        print i,j
        if i ** 2 + j ** 3 >= THRES:
            break
        for k in pl:
            v = PrimePower([i,j,k])
            if v >= THRES:
                break
            else:
                vset.add(v)
print len(vset)
