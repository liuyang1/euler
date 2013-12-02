def getDec(n):
    lst = []
    while n > 0:
        lst.append(n % 10)
        n /= 10
    return lst


def isPalind(n):
    lst = getDec(n)
    ln = len(lst)
    for i in range(ln / 2):
        if lst[i] == lst[ln - i - 1]:
            continue
        else:
            return False
    return True


def reverse(n):
    v = 0
    while n > 0:
        v = v * 10 + n % 10
        n = n / 10
    return v


COUNT = 50


def isLychrel(n):
    for i in range(COUNT):
        n += reverse(n)
        if isPalind(n):
            return False
    return True


cnt = 0
for i in range(1, 10**4):
    if isLychrel(i):
        print i
        cnt += 1
print cnt
