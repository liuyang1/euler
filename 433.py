def sgcd(x, y):
    cnt = 0
    while 1:
        x, y = y, x % y
        cnt += 1
        if y == 0:
            return cnt


def ssgcd(n):
    ss = n;
    for x in xrange(1, n + 1):
        print "\r%16d %16d" % (x, ss),
        for y in xrange(1, x):
            ss += 2 * sgcd(x, y) + 1
    return ss


for i in range(1, 40 + 1):
    for j in range(1, i):
        print "%d " % (sgcd(i,j)),
    print "*"
