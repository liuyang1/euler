from common.mymath import *
import itertools

max = 2143
isFound = 0
str = "123456789"
for j in range(9,0,-1):
    s = str[0:j]
    print j, " digits",s
    for i in itertools.permutations(s,j):
        n = "".join(i)
        n = int(n)
        if isPrime(n) and n > max:
            isFound = 1
            max = n
            print n
    if isFound == 1:
        break
