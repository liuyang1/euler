def getData():
    f = open("013.data")
    lst = []
    for l in f.readlines():
        l = int(l)
        lst.append(l)
    return lst

data = getData()
v = sum(data)
while v > 10**10:
    v = v / 10
print v
