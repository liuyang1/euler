
N = 10 ** 2
Square = frozenset([i ** 2 for i in range(1, 10**4)])


def isAllSquare(vv):
    for v in vv:
        if vv not in Square:
            return False
    return True


from itertools import count
for a in count(6):
    print a
    for z in range(1, a / 3):
        for y in range(z + 1, a / 2):
            x = a - y - z
            v = (x + y, x - y, x + z, x - z, y + z, y - z)
            if isAllSquare(v):
                print x, y, z
                import sys
                sys.exit()
