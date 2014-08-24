slst = [1,4,9,16,25,36,49,64,81]
def mySqrt(n):
    for i in range(len(slst)):
        if n < slst[i]:
            break
    yield i
    rem = n - slst[i]
    ret = [i]
    while 1:
        rem *= 100
        for b in range(0,10):
            if ret.extend(b) * b < rem:
                continue
            else
                break
        ret = rem - ret.extend(b)

s = mySqrt(2)
for i in range(10):
    print s.next()
