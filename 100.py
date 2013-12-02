from math import sqrt
def TestSqrt(n):
    a = n % 100
    b = n % 10
    if b != 0 and a != 25 and b != 1 and b !=4 and b != 6 and b!= 9:
        raise "no sqrt"
    s = int(sqrt(n))
    if s * s == n:
        return s
    else:
        raise "no sqrt"


i = 10**0
import sys
while 1:
    ii = 2 * i * (i - 1) + 1
    try:
        s = TestSqrt(ii)
    except:
        i += 1
        continue
    print i,(s + 1) / 2
    sys.stdout.flush()
    i += 1
# 4 3
# 21 15
# 120 85
# 697 493
# 4060 2871
# 23661 16731
# 137904 97513
# 803761 568345
# 4684660 3312555
# 27304197 19306983
