from common.mymath import *

l = PrimeLst(100)

thres = 10**6
v = 1
for i in l:
    v *= i
    if v >= thres:
        break
    print v
