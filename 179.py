def cntDivisor(n):
    """
    >>> cntDivisor(14)
    4
    >>> cntDivisor(140)
    12
    """
    rem = 1
    cnt = 2
    while 1:
        rem += 1
        num = n / rem
        if num < rem:
            break
        if n % rem == 0:
            cnt += 2
            if num == rem:
                cnt -= 1
                break
    return cnt


if __name__ == "__main__":
    lastcnt = 2
    CNT = 0
    for i in range(3, 10 ** 5):
        cnt = cntDivisor(i)
        if lastcnt == cnt:
            CNT += 1
        lastcnt = cnt
    print CNT
