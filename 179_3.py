"""
better, like Sieve algo.
ref as JohnMorris's method.
"""
if __name__ == "__main__":
    thresh = 10 ** 7
    lst = [1 for i in xrange(thresh + 1)]
    for i in xrange(2, thresh):
        for j in xrange(0, thresh + 1, i):
            lst[j] += 1
    cnt = 0
    for i in xrange(2, thresh):
        if lst[i] == lst[i - 1]:
            cnt += 1
    print cnt
