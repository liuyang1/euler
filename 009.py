def genTriple(s):
    for a in range(1, s / 3):
        for b in range(a, s / 2):
            c = s - a - b
            yield (a, b, c)


g = genTriple(1000)
while 1:
    a, b, c = g.next()
    if a ** 2 + b ** 2 == c ** 2:
        print a * b * c
        break
