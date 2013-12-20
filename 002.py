def func(thresh):
    a = 1
    b = 1
    ret = 0
    while 1:
        a, b = a + b, a
        if a > thresh:
            return ret
        if a % 2 == 0:
            ret += a

print func(4*1000*1000)
