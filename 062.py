import sys
from common import mymath


def search():
    m = {}
    destFreq = 5
    for i in range(10000):
        v = i ** 3
        freq = mymath.hashDigitCounter(v)
        print(v, freq)
        if freq not in m.keys():
            m[freq] = 1
        else:
            m[freq] += 1
            if m[freq] == destFreq:
                ret = freq
                break


def enumRet():
    ret = mymath.hashDigitCounter(589323567104)
    print("list...", ret)
    for i in range(10000):
        v = i ** 3
        freq = mymath.hashDigitCounter(v)
        if freq == ret:
            print(i, v, freq)
            break

if __name__ == "__main__":
    # search()
    enumRet()
