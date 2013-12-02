def ProdMod(a, b, n):
    return (a % n) * (b % n) % n


def PowerMod(a, b, n):
    if b <= 1:
        return a % n
    v = PowerMod(a, b / 2, n)
    v = (v * v) % n
    if b % 2 == 0:
        return v
    else:
        return (a * v) % n

v = PowerMod(2, 7830457, 10 ** 10)
v = ProdMod(28433, v, 10 ** 10)
v += 1
print v
