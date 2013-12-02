
def getData():
    fp = open("059_cipher.txt","r")
    for line in fp.readlines():
        l = [int(i) for i in line.split(',')]
    return tuple(l)

data = getData()
from collections import Counter
cdata = Counter(data)

print cdata
print len(cdata.keys())
