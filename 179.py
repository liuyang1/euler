def cntDivisor(n):
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


lastcnt = 2
CNT = 0
for i in range(3, 10 ** 7):
    cnt = cntDivisor(i)
    if lastcnt == cnt:
        CNT += 1
        print CNT, i - 1, i, cnt
    lastcnt = cnt
print CNT
