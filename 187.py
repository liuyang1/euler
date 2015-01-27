#! /usr/bin/env python2

from common import mymath

thresh = 10 ** 8
Plst = mymath.PrimeLst(thresh)

cnt = 0
for idx, i in enumerate(Plst):
    if i * i > thresh:
        break
    print i, cnt
    for j in Plst[idx:]:
        if i * j < thresh:
            cnt += 1
        else:
            break
print cnt
