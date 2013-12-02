def getSumDigit(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s


vm = 0
for a in range(1,100+1):
    for b in range(1,100+1):
        v = a ** b
        v = getSumDigit(v)
        if vm < v:
            vm = v
print vm
