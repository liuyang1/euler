l = [i * (i - 1) / 2 for i in range(2,10**6*2)]

mv = 2*10**6
DST = 2*10**6
for i in xrange(0,len(l)):
    pi = l[i]
    for j in xrange(i,len(l)):
        pj = l[j]
        p = pi * pj
        ad = abs(p - DST)
        if ad < mv:
            mv = ad
            print i,pi,j,pj,p,mv
