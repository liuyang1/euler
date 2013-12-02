def cntComThres(n, thres):
    """
    计算n的组合数大于thres的个数有多少个.
    """
    ret = 1
    r = 0
    while ret <= thres:
        r += 1
        # 迭代计算C(n, r)
        ret *= n - r + 1
        ret /= r
        # 如果计算超过一半,则说明组合数都小于阈值
        if r == n / 2 + 1:
            return 0
    # 返回剩余组合数,其大于thres
    return n + 1 - 2 * r


cnt = 0
for n in range(1, 100 + 1):
    cnt += cntComThres(n, 10 ** 6)
    print cnt
