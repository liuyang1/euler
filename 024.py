import itertools

n = 0
for i in itertools.permutations("0123456789",10):
    n += 1
    if n == 10**6:
        print "".join(i)
        break
