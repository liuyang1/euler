from common.mymath import *

def div(n):
    lst = []
    d = 1
    dlst = [1]
    while 1:
        d *= 10
        lst.append(d / n)
        d = d % n
        if d == 0:
            return (lst,0)
        for di in range(len(dlst)-1,-1,-1):
            if d == dlst[di]:
                return (lst,len(dlst)-di)
        dlst.append(d)
    return lst

max = 0
for i in range(2,1000):
    (lst, cnt) = div(i)
    if cnt > max:
        max = cnt
        print i
        print lst,cnt
