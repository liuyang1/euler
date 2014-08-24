def pentagon(n):
    return n * (3 * n - 1) / 2

N = 10**7
PentLst = []
for i in xrange(N*2):
    PentLst.append(pentagon(i))

PentSet = frozenset(PentLst)

NN = N + 0.0
maxv = max(PentSet)
for i in range(1680, N):
    pi = PentLst[i]
    j = i + 1
    pj1 = PentLst[j]
    while 1:
        pj = pj1
        j += 1
        pj1 = PentLst[j+1]
        s = pi + pj
        if s < pj1:
            break
        if s in PentSet:
            ss = s + pj
            print "%16d %16d %16d %16d" % (pi, pj, s, i)
            if ss in PentSet:
                print "%16d %16d %16d %16d" % (pi, pj, s, ss)
                import sys
                sys.exit()
            else:
                if ss > maxv:
                    raise Exception("fatal error");
