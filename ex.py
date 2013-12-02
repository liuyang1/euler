def pentagnonal(n):
    return (n * ( 3 * n - 1)) // 2

def generalised_pentagonal(n):
    if n % 2 == 0:
        return pentagnonal((n//2) + 1)
    else:
        return pentagnonal(-(n//2) - 1)

def termsign(i):
    if i % 4 < 2:
        return 1
    else:
        return -1

pt = [1]
for n in range(1,100+1):
    r, i = 0, 0
    while 1:
        k = generalised_pentagonal(i)
        if k > n:
            break
        r += termsign(i) * pt[n-k]
        i += 1
    pt.append(r)

print pt[1:]
