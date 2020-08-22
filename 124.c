#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/** https://projecteuler.net/problem=124
 * ordered radicals
 */

static bool isPrime(int n) {
    int i;
    if (n % 2 == 0) {
        return true;
    }
    for (i = 3; i * i <= n; i += 2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int *primes(int up, int *out_n) {
    int *p = malloc(sizeof(int) * up);
    int i, n;
    for (i = 2, n = 0; i != up; i++) {
        if (isPrime(i)) {
            p[n++] = i;
        }
    }
    if (out_n) {
        *out_n = n;
    }
    return p;
}
/** radical: product of all prime factors */
int rad(int n, int *primes, int primes_n) {
    int i, r;
    for (i = 0, r = 1; n != 1 && i < primes_n; i++) {
        int p = primes[i], f;
        if (p * p > n) {
            r *= n; /** 1, self */
            break;
        }
        for (f = 0; n % p == 0; f++) {
            n /= p;
        }
        if (f != 0) {
            r *= p;
        }
    }
    return r;
}

void show_int_arr(int *xs, int n) {
    int i;
    for (i = 0; i != n; i++) {
        printf("%d, ", xs[i]);
    }
    printf("\nnum:%d\n", n);
}
typedef struct {
    int n, r;
} Pair;

int cmppair(const void *a, const void *b) {
    const Pair *x = a, *y = b;
    if (x->r != y->r) {
        return x->r - y->r;
    }
    return x->n - y->n;
}

#define NMAX (1000 * 100)

int main() {
    int primes_n;
    int *prime = primes(NMAX, &primes_n);
#if 0
    show_int_arr(prime, primes_n);
    return 0;
#endif
    int i;
    Pair *xs = malloc(sizeof(Pair) * NMAX);
    for (i = 0; i != NMAX; i++) {
        Pair pr = {.n = i + 1, .r = rad(i + 1, prime, primes_n)};
        xs[i] = pr;
    }
    qsort(xs, i, sizeof(Pair), cmppair);
    int target = 10 * 1000 - 1; // C index from 0
    Pair x = xs[target];
    printf("%d %d\n", x.n, x.r);
    /** ans: 21417 */
    free(prime);
    free(xs);
    return 0;
}
