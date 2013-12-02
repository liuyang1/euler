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
        # return partitionEx(n, n - 1) + 1
#    return partitionEx(n, m - 1) + partitionEx(n - m, m)
        return partition(n, n - 1) + 1
    return partition(n, m - 1) + partition(n - m, m)


N = 10 ** 2
for i in range(1, N):
    v = partition(i, i)
    print i, v
    if v % 10 ** 3 == 0:
        print i
        break
