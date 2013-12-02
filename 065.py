# 2/1 3/1 8/3 11/4 19/7 87/32

class eSeq():
    def __init__(self):
        self.lst = [2]
        self.size = -1
        self.k = 1
    def __getitem__(self,i):
        if i > self.size:
            while self.size <= i:
                self.lst.extend([1, 2 * self.k, 1])
                self.k += 1
                self.size += 3
            return self.lst[i]
        else:
            return self.lst[i]

eseq = eSeq()

def eExpan(n):
    n -= 1
    p, q = eseq[n], 1
    while n > 0:
        n -= 1
        p, q = p * eseq[n] + q, p
    return (p, q)

p, q = eExpan(100)
print p

def getSumDigit(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s

print getSumDigit(p)
