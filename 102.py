def triangleArea(a, b, c):
    """
    calc area of triangle
    """
    ret = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    ret -= a[1] * b[0] + b[1] * c[1] + c[1] * a[0]
    return ret * 0.5


def triangleInside(a, b, c, pt):
    sc = triangleArea(a, b, pt)
    sa = triangleArea(b, c, pt)
    sb = triangleArea(c, a, pt)
    lst = [sc, sa, sb]
    lst = sum([1 if i > 0 else 0 for i in lst])
    return lst == 3 or lst == 0

origin = [0, 0]


def test():
    a = [-340, 495]
    b = [-153, -910]
    c = [835, -947]
    print triangleInside(a, b, c, origin)
    x = [-175, 41]
    y = [-421, -714]
    z = [574, -645]
    print triangleInside(x, y, z, origin)


def load(fn):
    with open(fn) as fp:
        ret = []
        for line in fp.readlines():
            line = line.split(",")
            lst = [int(i) for i in line]
            vec = [lst[i:i + 2] for i in range(0, len(lst), 2)]
            ret.append(vec)
        return ret

data = load("data.102")
s = 0
for d in data:
    d.append(origin)
    s += triangleInside(*d)
print s
