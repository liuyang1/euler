# freq: first is whitespace char, next is 'e'
from collections import Counter


def getData():
    fp = open("059_cipher.txt", "r")
    for line in fp.readlines():
        l = [int(i) for i in line.split(',')]
    return tuple(l)


def FreqCounter(lst):
    c = Counter(lst)
    s = [(n, f) for n, f in c.iteritems()]
    s = sorted(s, key=lambda x: -1 * x[1])
    return s
data = getData()
l = 3
d = [data[i::l] for i in range(l)]
# ===========
cipher = 'god'
# ===========
ret = ""
for idx, r in enumerate(data):
    p = r ^ ord(cipher[idx % l])
    ret += chr(p)
print ret
print sum([ord(i) for i in ret])
