def DotProdLst(lst, a):
    return [a*i for i in lst]


def ShiftLst(lst, n):
    t = [0] * n
    return t + lst


def AddLst(lst1, lst2):
    if len(lst1) < len(lst2):
        lst1, lst2 = lst2, lst1
    if len(lst1) > len(lst2):
        lst2 += [0] * (len(lst1) - len(lst2))
    t = zip(lst1, lst2)
    t = [x + y for x, y in t]
    return t


def ProdLst(lst1, lst2):
    if len(lst1) < len(lst2):
        lst1, lst2 = lst2, lst1
    ret = [0]
    for i in range(len(lst2)):
        v2 = lst2[i]
        t = DotProdLst(lst1, v2)
        ret = AddLst(ShiftLst(t, i), ret)
    return ret

    
def PowerLst(lst, n):
    if n <= 0:
        return []
    if n == 1:
        return lst
    if n % 2 == 0:
        v = PowerLst(lst, n / 2)
        return ProdLst(v, v)
    else:
        v = PowerLst(lst, n / 2)
        return ProdLst(ProdLst(v, v), lst)

colin = PowerLst([0] + [1] * 6, 6)
peter = PowerLst([0] + [1] * 4, 9)

colin = DotProdLst(colin, 1.0 / sum(colin))
peter = DotProdLst(peter, 1.0 / sum(peter))

ans = 0
for i in range(len(peter)):
    v = sum(colin[0:i])
    v *= peter[i]
    ans += v
print round(ans * 10 ** 7) * 10 ** (-7)
