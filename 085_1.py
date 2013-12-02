#-*- encoding=utf8 -*-
trilst = (i * (i - 1) / 2 for i in range(2, 1414 + 1 + 1))
trilst = list(trilst)

def getNearst(sortedlst, v):
    '''
    对已经排序好的序列,取得最接近v的值
    '''
    while 1:
        if len(sortedlst) == 1:
            return sortedlst[0]
        elif len(sortedlst) == 2:
            d0 = abs(sortedlst[0] - v)
            d1 = abs(sortedlst[1] - v)
            if d1 < d0:
                return sortedlst[1]
            elif d0 < d1:
                return sortedlst[0]
            else:
                return sortedlst
        half = len(sortedlst) / 2
        halfv = sortedlst[half]
        if halfv == v:
            return v
        elif halfv > v:
            sortedlst = sortedlst[0:half + 1]
        else:
            sortedlst = sortedlst[half:]


DST = 2.0 * 10 ** 6
dd = DST
for i in trilst:
    v = DST / i
    if v < i:
        print "final"
        break
    vn = getNearst(trilst, v)
    d = abs(vn * i - DST)
    if d < dd:
        dd = d
        m = trilst.index(i)
        n = trilst.index(vn)
        print (m + 1) * (n + 1)
