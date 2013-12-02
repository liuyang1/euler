def triangle(m):
    l = []
    n = 1
    while 1:
        v = n * (n + 1) / 2
        if v > m:
            break
        n += 1
        l.append(v)
    return l


def pentagon(m):
    l = []
    n = 1
    while 1:
        v = n * (3 * n - 1) / 2
        if v > m:
            break
        n += 1
        l.append(v)
    return l


def hexagon(m):
    l = []
    n = 1
    while 1:
        v = n * (2 * n - 1)
        if v > m:
            break
        n += 1
        l.append(v)
    return l


th = 10**10
tri = frozenset(triangle(th))
pen = frozenset(pentagon(th))
hex = frozenset(hexagon(th))

s = tri & pen & hex

print s


