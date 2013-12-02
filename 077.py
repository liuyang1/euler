from common.mymath import *
print PrimeLst(100)

def PrimePart(n, m):
    if n == 1 or m == 1:
        return 1
    if n <= m:
        return PrimePart(n, n - 1) + 1
    return PrimePart

