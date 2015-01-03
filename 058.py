#! /usr/bin/env python2


"""
generate square sequence number
simply checking isPrime
"""
class square():

    def __init__(self):
        self.s = 1
        self.l = 2
        self.i = 0

    def next(self):
        """
        >>> sq= square()
        >>> [sq.next() for i in range(12)]
        [3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49]
        """
        if self.i == 4:
            self.i = 0
            self.l += 2
        self.i += 1
        self.s += self.l
        return self.s

    def length(self):
        return self.l + 1

if __name__ == "__main__":
    from common import mymath
    # start with cnt as 1, as first number 1
    primecnt, cnt = 0, 1
    sq = square()
    while 1:
        num = sq.next()
        cnt += 1
        if mymath.isPrime(num):
            primecnt += 1
        if primecnt * 10 < cnt:
            # print num, primecnt, cnt, primecnt / (cnt + 0.), sq.length()
            print sq.length()
            break
