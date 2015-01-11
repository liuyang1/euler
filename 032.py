def digit2num(d):
    n = 0
    for i in d:
        n = 10 * n + i
    return n

from common import mymath
import itertools


def search():
    seq = range(1, 10)
    # 1, 4, 4, 2
    # 2, 3, 4, 7
    # 2, 2, 5 NONE
    first = 2
    second = 2
    for i in itertools.permutations(seq, first):
        other = [x for x in seq if x not in i]
        x = digit2num(i)
        for j in itertools.permutations(other, second):
            y = digit2num(j)
            zz = x * y
            zd = mymath.hashDigitCounter(zz)
            if any([t > 1 for t in zd]):
                continue
            last = [x for x in other if x not in j]
            tp = [0 for i in range(0, 10)]
            for i in range(0, 10):
                if i in last:
                    tp[i] = 1
            tp = tuple(tp)
            if zd == tp:
                print(x, y, zz)

ret = sum([5796, 5346, 4396, 7254, 7632, 6952, 7852])
print(ret)
# 45228
