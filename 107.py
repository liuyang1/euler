from decimal import Decimal

inf = Decimal('Infinity')

def getData():
    # with open("data.107.example") as f:
    with open("data.107") as f:
        ret = []
        for l in f.readlines():
            l = l.replace('-','0')
            l = l.split(',')
            l = [int(i) for i in l]
            ret.append(l)
        return ret

def infinite(data):
    size = len(data)
    for i in range(size):
        for j in range(size):
            data[i][j] = inf if data[i][j] is 0 else data[i][j]
    return data


def miniNetwork(net):
# find mini
    s = 0
    v = inf
    for i, row in enumerate(net):
        for j, val in enumerate(row):
            if val < v:
                v = val
                netset = {i, j}
    s += v
    allset = set(range(len(net))) - netset
    while 1:
        v = inf
        for b in netset:
            for e in allset:
                if net[b][e] < v:
                    v = net[b][e]
                    em = b, e
        s += net[em[0]][em[1]]
        netset.add(em[1])
        allset.remove(em[1])
        if len(allset) == 0:
            break
    print "total weights of minimal network: ", s
    return s

data = getData()
s = sum(sum(row) for row in data)
s = s / 2
print "origin total weights: ", s
data = infinite(data)
m = miniNetwork(data)
print "saving: ", s - m
