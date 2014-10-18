import itertools


def digit(num):
    lst = []
    while num > 0:
        lst.append(num % 10)
        num /= 10
    return lst


def isBouncy(dig):
    p = [(dig[i], dig[i + 1]) for i in range(len(dig) - 1)]
    dec = all([a >= b for a, b in p])
    inc = all([a <= b for a, b in p])
    return not (dec or inc)

p0 = 0.99
cnt = 0
for i in itertools.count(100):
    if isBouncy(digit(i)):
        cnt += 1
    if cnt == i * p0:
        print "ans: ", cnt, i
        break
    else:
        print cnt / (i + 0.0), cnt, i
