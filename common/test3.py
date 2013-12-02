import math


def isPrime(n):
    if n==1 or n==2:
        return True
    i=2
    thres = math.sqrt(n)
    while i<=thres:
        if n%i==0:
            return False
        i += 1
    return True

def isCons(lst,i,n):
    for j in range(n-1):
        if(lst[i+j]+1==lst[i+j+1]):
            pass
        else:
            return False
    return True

import operator
def prod(factors):
    return reduce(operator.mul,factors,1)


def isPytha(a,b,c):
    if a * a + b * b == c * c:
        return True
    return False

#(a, b, c) = (1, 2, 1000-1-2)

def next(a,b,c):
    if b+1<=c-1:
        return (a,b+1,c-1)
    else:
        if a+2<1000-a-a-3:
            return (a+1,a+2,1000-a-a-3)
        else:
            raise Exception("no next")

lst = []
while 1:
    try:
        line = raw_input()
    except:
        break
    line = [int(i) for i in line.split()]
    lst.append(line)
print lst


