import operator
def maxAdjMul(a, n):
    aa = [a[i:] for i in range(n)]
    aa = zip(*aa)
    return max([reduce(operator.mul, i) for i in aa])

def getData():
    with open("data.008") as f:
        lst = []
        for l in f.readlines():
            l = l.strip()
            l = [int(i) for i in l]
            lst.extend(l)
    return lst

data = getData()
print maxAdjMul(data, 13)
