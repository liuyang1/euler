def spiral():
    a, l = 1, 2
    yield a
    while 1:
        for i in range(4):
            a += l
            yield a
        l += 2

sp = spiral()
n = 1001
s = 0
for i in range(2 * n - 1):
    s += sp.next()
print s
