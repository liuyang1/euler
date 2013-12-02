#C(a + b, a)
def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1)


def com(a, b):
    al = xrange(a - b + 1, a + 1)
    bl = xrange(1, b + 1)
    return prod(al) / prod(bl)


def lattice(m, n):
    return com(m + n, m)

print lattice(2, 2)
print lattice(20, 20)
