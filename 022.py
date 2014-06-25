def getData():
    with open("data.022") as f:
        for l in f.readlines():
            l = l.split(',')
            l = [i[1:-1] for i in l]
            return l

def Char2Order(c):
    return ord(c) - ord('A') + 1

def Name2Score(name):
    return sum([Char2Order(c) for c in name])


def sumNameScores(data):
    data.sort()
    data = [(idx + 1) * Name2Score(n) for idx, n in enumerate(data)]
    return sum(data)


data = getData()
print sumNameScores(data)
