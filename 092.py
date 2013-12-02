def getSumDigitSquare(n):
    cnt = 0
    while n:
        cnt += (n % 10) ** 2
        n /= 10
    return cnt


set1 = set([1])
set89 = set([89])

for i in range(1, 10 ** 7):
    n = i
    while 1:
        if n in set1:
            set1.add(i)
            break
        elif n in set89:
            set89.add(i)
            break
        n = getSumDigitSquare(n)

print len(set89)
