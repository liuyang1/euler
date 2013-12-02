def sumDivsor(k):
    if k == 1:
        return 1
    cnt = 0
    for i in xrange(1, k):
        if k % i == 0:
            r = k / i
            if i > r:
                break
            cnt += i
            if i != r:
                cnt += r
    return cnt


def Sn(n):
    s = 0
    for i in range(1, n + 1):
        print i
        s += sumDivsor(i * i)
        for j in range(i + 1, n + 1):
            s += 2 * sumDivsor(i * j)
    return s


print Sn(10 ** 5)
