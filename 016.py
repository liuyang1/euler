def sumDigit(n):
    return sum([int(i) for i in str(n)])


print sumDigit(2**1000)
