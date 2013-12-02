

kls = [200, 100, 50, 20, 10, 5, 2, 1]

s = 200

def coin(n,kls):
    if len(kls)==1:
        return 1
    s = 0
    for i in range(0,n/kls[0]+1):
        rem = n-i*kls[0]
        if rem>0:
            s += coin(n-i*kls[0], kls[1:])
        else:
            s += 1
            break
    return s
print 200,coin(200,kls)
