def loaddata():
    with open('011.data') as f:
        ret = []
        for l in f.readlines():
            ret.append([int(i) for i in l.split()])
        return ret


def prod(lst):
    return reduce(lambda x, y: x * y, lst, 1)


data = loaddata()

max = 0
for j in xrange(0, len(data)):
    for i in xrange(0, len(data) - 4):
        v = prod(data[j][i: i + 4])
        if v > max:
            max = v
print max

diag = []
for j in xrange(0, 2 * len(data) - 1):
    t = []
    for i in xrange(0, j + 1):
        k = j - i
        if i >= 20 or k >= 20:
            continue
        t.append(data[i][k])
    diag.append(t)

for l in diag:
    for i in xrange(0, len(l) - 4):
        v = prod(l[i: i + 4])
        if v > max:
            max = v
print max


data = map(list, zip(*data))
for j in xrange(0, len(data)):
    for i in xrange(0, len(data) - 4):
        v = prod(data[j][i: i + 4])
        if v > max:
            max = v
print max


diag = []
for j in xrange(0, 2 * len(data) - 1):
    t = []
    for i in xrange(0, j + 1):
        k = j - i
        if i >= 20 or k >= 20:
            continue
        t.append(data[i][k])
    diag.append(t)

for l in diag:
    for i in xrange(0, len(l) - 4):
        v = prod(l[i: i + 4])
        if v > max:
            max = v
print max
