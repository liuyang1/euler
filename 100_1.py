
class Square():
    def __init__(self):
        self.mset = set([1]) 
        self.mk = 1
        self.mv = 1
    def __contains__(self,n):
        if n < self.mv:
            return n in self.mset
        else:
            from math import sqrt
            mk = int(sqrt(n)) + 2
            for i in xrange(self.mk, mk, 2):
                self.mset.add(i ** 2)
            self.mk = mk
            self.mv = mk ** 2
            return n in self.mset


s = Square()
print 10**12 in s
print (10**12)**2 in s
print (10**12+1)**2 in s
