from functools import wraps
import sys


def memo(func):
    cache = {}

    @wraps(func)
    def wrap(*arg):
        if arg not in cache:
            cache[arg] = func(*arg)
        print cache
    return wrap


class TailRecurseException:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs


def tailcall(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and \
                f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
        else:
            while 1:
                try:
                    return g(*args, **kwargs)
                except TailRecurseException, e:
                    args = e.args
                    kwargs = e.kwargs
    return func


@tailcall
def cntCollatz(n, acc=0):
    if n == 1:
        return acc
    if n % 2 == 0:
        return cntCollatz(n / 2, acc + 1)
    else:
        return cntCollatz(3 * n + 1, acc + 1)

print cntCollatz(13)
sys.exit()
mv = 0
mi = 1
for i in range(10 ** 6, 0, -1):
    v = cntCollatz(i)
    print "%10d %10d\t%10d %10d" % (i, v, mi, mv)
    if v > mv:
        mv = v
        mi = i
