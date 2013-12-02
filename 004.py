def getDec(n):
    lst = []
    while n>0:
        lst.append(n%10)
        n /= 10
    return lst


def isPalind(n):
    lst = getDec(n)
    ln = len(lst)
    for i in range(ln/2):
        if lst[i] == lst[ln-i-1]:
            continue
        else:
            return False
    return True


import sys
n = 999999
while 1:
    if isPalind(n):
        for a in range(100,1000):
            if n % a == 0:
                b = n / a
                if b>=100 and b < 1000:
                    print a,b,n
                    sys.exit()
    n -= 1
