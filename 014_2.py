def cntCollatz(n):
    cnt = 0
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return cnt


m = 0
mv = 0
thres = 10 ** 6
for i in xrange(thres / 2, thres + 1):
    t = cntCollatz(i)
    if t > mv:
        mv = t
        m = i
print m, mv
