def getData():
    f = open("082.1.data")
    data = [[int(i) for i in l.split(',')] for l in f.readlines()]
    return map(list,zip(*data))# trans

data = getData()

def acc(p1,idx):
    pn = [0 for i in range(len(p1))]
    cs = 0
    for i in range(idx - 1, -1, -1):
        cs += p1[i]
        pn[i] = cs
    cs = 0
    for i in range(idx + 1, len(p1), 1):
        cs += p1[i]
        pn[i] = cs
    return pn

def myAdd(p0, p1):
    ret = []
    for i in range(len(p1)):
        pn = acc(p1,i)
        ret.append(min(map(lambda x, y: x + y, p0, pn)) + p1[i])
    return ret
        


p0 = data[0]
for j in range(1,len(data)):
    p1 = data[j]
    p0 = myAdd(p0, p1)
print min(p0)
