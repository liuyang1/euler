def solve(sdk):


def getSudoku():
    with open('096.data') as f:
        cnt = 0
        lst = []
        for line in f.readlines():
            if cnt != 0:
                line = line.strip()
                line = [int(i) for i in line]
                lst.append(line)
            cnt += 1
            if cnt == 10:
                yield lst
                cnt = 0
                lst = []

def main():
    sudoku = getSudoku()
    for i in range(50):
        print sudoku.next()


if __name__ == "__main__":
    main()
