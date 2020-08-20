#include <string.h>
#include <stdio.h>
#include <stdlib.h>
/** https://projecteuler.net/problem=179
 * find all n, n+1 have same number of factors
 */

#define NMAX (1000 * 1000 * 10)
#define NSQT (1000 * 1000 * 5)

/** simple, but slow
 * It's O(n)
 */
int factorCnt(int n) {
    int i, cnt;
    for (i = 2, cnt = 0; i <= n / 2; i++) {
        cnt += n % i == 0;
    }
    return cnt + 2; /* 1 & self */
}

int *primes(int up, int *n) {
    char *st = malloc(up);
    memset(st, 0x01, up);
    int i, j, cnt; /** sieve method */
    for (i = 2, cnt = 0; i != up; i++) {
        if (st[i]) {
            for (j = 2 * i; j < up; j += i) {
                st[j] = 0;
            }
            cnt++;
        }
    }
    int *xs = malloc(up);
    for (i = 2, j = 0; i != up; i++) {
        if (st[i]) {
            xs[j++] = i;
        }
    }
    if (n) {
        *n = j;
    }
    free(st);
    return xs;
}
/** Its O(prime(n)) */
int factorCnt2(int n, int *primes, int primes_n) {
    int i, cnt;
    for (i = 0, cnt = 1; n != 1 && i < primes_n; i++) {
        int p = primes[i], f;
        if (p * p > n) {
            cnt *= 2; /** 1, self */
            break;
        }
        for (f = 0; n % p == 0; f++) {
            n /= p;
        }
        cnt *= f + 1;
    }
    return cnt;
}

void show_int_arr(int *xs, int n) {
    int i;
    for (i = 0; i != n; i++) {
        printf("%d, ", xs[i]);
    }
    printf("\nnum:%d\n", n);
}

int main() {
    int primes_n;
    int *prime = primes(NSQT, &primes_n);
    // show_int_arr(prime, primes_n);
    // return 0;
    int i, cnt = 0;
    int n0, n1;
    n1 = factorCnt(2);
    for (i = 2; i != 1000 * 1000 * 10; i++) {
        // n0 = n1, n1 = factorCnt(i + 1);
        n0 = n1, n1 = factorCnt2(i + 1, prime, primes_n);
        cnt += n0 == n1;
#if 0
        if (i % (1000 * 100) == 0) {
            printf("%d %d\n", i, cnt);
        }
#endif
#if 0
        if (n0 == n1) {
            printf("%d %d %d\n", i, i + 1, n0);
        }
#endif
    }
    printf("%d\n", cnt);
    /** ans: 986262 */
    free(prime);
    return 0;
}
