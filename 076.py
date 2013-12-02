retMap = {(1, 1): 1}


def partitionEx(n, m):
    global retMap
    if (n, m) in retMap.keys():
        return retMap[(n, m)]
    else:
        retMap[(n, m)] = partition(n, m)
        return retMap[(n, m)]


def partition(n, m):
    if n == 1 or m == 1:
        return 1
    if n <= m:
        return partitionEx(n, n - 1) + 1
    return partitionEx(n, m - 1) + partitionEx(n - m, m)


N = 10**2
print partition(N, N - 1)
