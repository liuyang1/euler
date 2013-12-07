#! /usr/bin/env python
def getDec(n):
    lst = []
    while n > 0:
        lst.append(n % 10)
        n /= 10
    return lst


def isPalind(n):
    lst = getDec(n)
    # faster than return lst1 == lst1.reverse()
    ln = len(lst)
    for i in range(ln / 2):
        if lst[i] == lst[ln - i - 1]:
            continue
        else:
            return False
    return True


maxval = 0
for x in xrange(1000, 100, -1):
    for y in xrange(x, 100, -1):
        p = x * y
        if p > maxval and isPalind(p):
            maxval = p
print maxval
