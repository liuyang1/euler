def getData():
    with open("107.data") as f:
        ret = []
        for l in f.readlines():
            l = l.replace('-','0')
            l = l.split(',')
            l = [int(i) for i in l]
            ret.append(l)
        return ret


def Prime(data):
    m = len(data)
    n = len(data[0])
    print m, n
    ret = [[0] * n] * m
    print ret
    print min(min(data))



print Prime([[1,2],[3,4]])
