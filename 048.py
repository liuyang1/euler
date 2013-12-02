s = 0
for i in range(1,1000):
    s += i**i
    s = s % 10**10
print s
