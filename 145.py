def rev(n):
    v = 0
    while n > 0:
        v = v * 10 + n % 10
        n = n / 10
    return v


def isOddDigit(n):
    while n:
        r = n % 10
        if r % 2 == 0:
            return False
        n = n / 10
    return True


def main():
    N = 10 ** 7
    cnt = 0
    for n in xrange(1, N):
        if n % 10 == 0:
            continue
        if isOddDigit(n + rev(n)):
            cnt += 1
    print cnt


if __name__ == "__main__":
    main()
