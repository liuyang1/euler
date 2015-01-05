def loadData():
    with open("079.data") as fp:
        lst = []
        for line in fp.readlines():
            v = int(line)
            if v not in lst:
                lst.append(v)
        return lst

d = loadData()
from common import mymath

for i in d:
    dd = mymath.digit(i)
    if True:
        print i,
print "ret", 73162890
