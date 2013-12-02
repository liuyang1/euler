from itertools import product

lst = (True, False)


tbl = [i for i in product(lst, repeat = 6)]

def genTruthTbl():
    for i in product(lst, repeat = len(tbl)):
        yield dict(zip(tbl, i))

print len(tbl), 2 ** len(tbl), "to check"
tb = genTruthTbl()
cnt = 0
while 1:
    TB = tb.next()
    tcnt = 0
    for t in tbl:
        n = t[0] != (t[1] and t[2])
        nt = tuple(list(t[1:]) + [n])
        v1 = TB[t]
        v2 = TB[nt]
        if v1 and v2 != 0:
            break
        else:
            tcnt += 1
    if tcnt == len(tbl):
        cnt += 1
        print cnt
print cnt
