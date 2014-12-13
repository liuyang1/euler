from common import mymath
from itertools import count

if __name__ == "__main__":
    foundFlag = False
    for i in count(10 ** 5):
        n, nn = i, i
        freq = mymath.digitCounter(n)
        print n,
        for j in xrange(2, 7):
            nn = nn + n
            print nn,
            nf = mymath.digitCounter(nn)
            if nf != freq:
                break
            if j == 6:
                foundFlag = True
                break
        if foundFlag:
            print n
            break
