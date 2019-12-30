import copy

def poly_lst(fn):
    lst = [fn(i) for i in range(10, 150)]
    lst = [i for i in lst if i > 999 and i <= 9999 ]
    return lst


fn_lst = [lambda n: n * (n + 1) / 2,
        lambda n: n * n,
        lambda n: n * (3 * n - 1) / 2,
        lambda n: n * (2 * n - 1),
        lambda n: n * (5 * n - 3) / 2,
        lambda n: n * (3 * n - 2)]

ll = [poly_lst(f) for f in fn_lst]

def num2adj(n, label):
    return n / 100, n % 100, label

adjset = []

label = 3
for l in ll:
    adjset.extend(list(num2adj(i, label) for i in l))
    label += 1

adjset = sorted(adjset)

def same(p0, p1):
    return p0[0] == p1[0] and p0[1] == p1[1] and p0[2] == p1[2]


def search(st_lst):
    end = st_lst[-1]
    cand = [i for i in adjset if i[0] == end[1] and not any(i[2] == j[2] for j in st_lst)]
    return [st_lst + [i] for i in cand]

#print adjset[0:10]

def fmap(xs):
    lst = []
    for i in xs:
        l = search(i)
        lst.extend(l)
    return lst

st1 = [[i] for i in adjset]
st2 = fmap(st1)
st3 = fmap(st2)
st4 = fmap(st3)
st5 = fmap(st4)
st6 = fmap(st5)


def isCyclic(st_lst):
    return st_lst[0][0] == st_lst[-1][1]

st = [i for i in st6 if isCyclic(i)]
for i in st:
    print i
