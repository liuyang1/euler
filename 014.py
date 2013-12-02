CollatzMap = {1: 0}


def cntCollatzEx(n):
    if n in CollatzMap.keys():
        return CollatzMap[n]
    if n % 2 == 0:
        v = cntCollatzEx(n / 2) + 1
    else:
        v = cntCollatzEx(3 * n + 1) + 1
    CollatzMap[n] = v
    return v


mv = 0
mi = 1
for i in range(10 ** 6, 0, -1):
    v = cntCollatzEx(i)
    print "%10d %10d\t%10d %10d" % (i, v, mi, mv)
    if v > mv:
        mv = v
        mi = i
