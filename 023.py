from math import sqrt

def factorlst(n):
    l = set({1})
    thres = int(sqrt(n))
    for i in range(2,thres+1):
        if n % i == 0:
            l.add(i)
# maybe n/i == i,so use SET
            l.add(n / i)
    return l


def isAbundant(n):
    l = factorlst(n)
    if sum(l) > n:
        return True
    else:
        return False


l = []
for i in range(2,28123+1):
    if isAbundant(i):
        l.append(i)
abundantSet = frozenset(l)

l = []
for i in range(1,28123+1):
    for j in abundantSet:
        if j > (i + 1) / 2:
            l.append(i)
            break
        else:
            if i - j in abundantSet:
                print i, j, i - j
                break
print sum(l)
