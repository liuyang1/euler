def getDigit(s):
    return [int(i) for i in str(s)]


from itertools import product
from collections import Counter


st = set()
#for l in combinations([0,1,2,3,4,5,6,7,8,9], N):
for N in range(2,6+1):
    print N
    for l in product([0,1,2,3,4,5,6,7,8,9], repeat = N):
        s = sum([i**5 for i in l])
        ll = getDigit(s)
        l = Counter(l)
        ll = Counter(ll)
        if l == ll:
            st.add(s)

print st
print sum(st)
