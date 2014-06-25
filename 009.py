def genTriple(s):
    init = [1, 1, s - 2]
    yield init
    while 1:
        init[0] += 1
        init[-1] -= 1
        if init[0] > init[1] or init[0] > init[2] or init[1] > init[2]:
            init = [1, init[1] + 1, s - init[1] - 2]
            if init[1] > init[2]:
                return
        yield init

g = genTriple(1000)
while 1:
    a, b, c = g.next()
    print a, b, c,
    l, r = a ** 2 + b ** 2, c ** 2
    if a ** 2 + b ** 2 < c ** 2:
        print "-"
    elif l > r:
        print "+"
    else:
        print "="
        break
