import itertools

def chkDiv(nlst):
    factor = [2,3,5,7,11,13,17]
    for i in range(1,8):
        sub = nlst[i:i+3]
        sub = int("".join(sub))
        if sub % factor[i-1] != 0:
            return False
    return True

s = 0
for i in itertools.permutations("0123456789",10):
    if chkDiv(i):
        n = "".join(i)
        n = int(n)
        print n
        s += n
print s
