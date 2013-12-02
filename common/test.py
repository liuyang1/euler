import math

def defactor(n):
    if n==1:
        return 1
    factor = 2
    while factor<math.sqrt(n):
        if n%factor == 0:
            return factor
        factor += 1
    return n

def factorlst(n):
    lst = []
    while 1:
        factor = defactor(n)
        n /= factor
        lst.append(factor)
        if factor == n:
            break
    return lst
