from math import *


def isBigger(a, b):
    return a[1] * log(a[0]) > b[1] * log(b[0])


def getData():
    return [[int(i) for i in l.split(',')] for l in open("099.data").readlines()]

data = getData()
max = [1, 1]
for i in range(len(data)):
    if isBigger(data[i], max):
        max = data[i]
        print i + 1, data[i], data[i][1] * log(data[i][0])
