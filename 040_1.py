#! /usr/bin/python
# 得到数字n的第bit位(从左起)
def getNbit(n, bit):
    return int(str(n)[bit])


def cham(n):
    t = thresh()
    while 1:
        low, high, bit = t.next()
        if n <= high: #若t<high,则为此区间内
            offset = n - low                        # 本区间内的偏移量
            num = offset / bit + pow(10, bit - 1)   # 本区间偏移到具体哪个数字
            seq = offset % bit                      # 偏移到该数字的第几位
            ret = getNbit(num, seq)
            return ret


# 得到各个区间的阈值
# 1 9 1
# 10 189 2
# 190 2889 3
# 意思为长度为3的数据,占据的范围为从第190位到第2889位.
def thresh():
    low = 0
    bit = 1
    while 1:
        high = low + 9 * pow(10, bit - 1) * bit
        yield (low + 1, high, bit)
        bit += 1
        low = high

v = 1
for i in xrange(7):
    v *= cham(pow(10, i))
print v
