ruleMonth = [31, 28, 31, 30, 31,
        30, 31, 31, 30, 31,
        30, 31]


def isleap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def format(d):
    if isleap(d[0]):
        ruleMonth[2-1] = 29
    else:
        ruleMonth[2-1] = 28
    if d[2] > ruleMonth[d[1]-1]:
        d[1], d[2] = d[1]+1, 1
    if d[1] > 12:
        d[0], d[1], d[2] = d[0]+1, 1, 1
    if d[3] > 7:
        d[3] = 1
    return d

def date():
    d = [1900, 1, 1, 1]
    while 1:
        d[2], d[3] = d[2]+1, d[3] + 1
        d = format(d)
        yield d

g = date()
cnt = 0
while 1:
    d = g.next()
    if d[0] == 1901:
        break
while 1:
    if d[2] == 1 and d[3] == 7:
        cnt += 1
    d = g.next()
    if d[0] == 2000 and d[1] == 12 and d[2] == 31:
        break
print cnt
