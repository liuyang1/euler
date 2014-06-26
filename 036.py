def digit(n, base=10):
    lst = []
    while n > 0:
        lst.append(n % base)
        n /= base
    return lst

def isPalind(l):
    ln = len(l)
    return all([l[i] == l[ln - i - 1] for i in xrange(ln / 2)])

s = 0
for i in xrange(10 ** 6):
    d10 = digit(i, 10)
    if not isPalind(d10):
        continue
    d2 = digit(i, 2)
    if isPalind(d2):
        s += i
print s
