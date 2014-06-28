def triNum(thresh):
    a, n = 1, 1
    l = [a]
    while 1:
        n += 1
        a += n
        l.append(a)
        if a > thresh:
            break
    return l

def getData():
    with open("data.042") as f:
        for l in f.readlines():
            l = l.split(',')
            l = [i[1:-1] for i in l]
            return l

def Char2Order(c):
    return ord(c) - ord('A') + 1

def Word2Val(w):
    return sum([Char2Order(c) for c in w])

data = getData()
data = [Word2Val(w) for w in data]
m = max(data)
l = triNum(m)
print len([1 for i in data if i in l])
