def loadData():
    with open("054.data") as f:
        ret = []
        for line in f.readlines():
            line = line.split()
            ret.append(line)
        return ret

def isConsecutive(number):
    if max(number) - min(number) == 

def calcScore(player):
    number = [item[0] for item in player]
    colors = [item[1] for item in player]


if __name__ == "__main__":
    data = loadData()
    for entry in data:
        player1 = entry[:5]
        player2 = entry[5:]
        print player1
        print player2
        import sys
        sys.exit()
