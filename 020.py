
def factorial(n):
    l = range(1,n+1)
    import operator
    return reduce(operator.mul,l,1)


def sumDigit(n):
    s = str(n)
    return sum([int(i) for i in s])

print sumDigit(factorial(100))
