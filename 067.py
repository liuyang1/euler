def getData():
    f = open("067.data")
    return [[int(i) for i in l.split()] for l in f.readlines()]


data = getData()


def myAdd(l1, l2):
    assert len(l1) == len(l2) + 1
    return [l2[j] + max(l1[j], l1[j + 1]) for j in range(len(l2))]


l = [0 for i in range(len(data[-1]) + 1)]
for l2 in data[::-1]:
    l = myAdd(l, l2)
print l
