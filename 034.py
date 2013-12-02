def getFact():
    fact = [1]
    p = 1
    for i in range(1,10):
        p *= i
        fact.append(p)
    return fact

g_Fact = getFact()

def getDigit(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = n / 10
    return l


def getDigitFactSum(n):
    l = getDigit(n)
    l = [g_Fact[i] for i in l]
    return sum(l)


def isDigitFact(n):
    return n==getDigitFactSum(n)


print isDigitFact(145)

s = 0
i = 10
while i<10**10:
    try:
        if isDigitFact(i):
            s += i
            print i
        i += 1
    except:
        print i
        print "interupted"
        break
print s
