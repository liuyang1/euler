(b, a) = (1, 1)

cnt = 2
while 1:
    (b, a) = ( a + b, b)
    cnt += 1
    if b>=pow(10,999):
        break
print cnt,b
