def getData():
    f = open("081.data")
    return [[int(i) for i in l.split(',')] for l in f.readlines()]


data = getData()
#data = [[131,673,234],[201,96,342],[630,803,746]]
for k in range(0, 2 * len(data) - 1):
    for i in range(k + 1):
        j = k - i
        if j >= len(data) or i >= len(data):
            continue
        vtop = data[i - 1][j] if i > 0 else 0
        vlft = data[i][j - 1] if j > 0 else 0
        if i < 1:
            if j < 1:
                continue
            else:
                mv = data[i][j - 1]
        else:
            if j < 1:
                mv = data[i - 1][j]
            else:
                mv = min(data[i - 1][j], data[i][j - 1])
        data[i][j] += mv
        #print i,j,mv,data[i][j]

print data[-1][-1]

