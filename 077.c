#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/** https://projecteuler.net/problem=77
 * prime summations
 * prime partion with 5000 ways
 */

#define MIN(a, b) ((a) < (b) ? (a) : (b))
static bool isPrime(int n) {
    int i;
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
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
void show_int_arr(int *xs, int n, const char *label) {
    printf("%s: ", label);
    int i;
    for (i = 0; i != n; i++) {
        printf("%d, ", xs[i]);
    }
    printf("\n");
}

#define UNDEF (-1)
int primePartR(int n, int *prime, int primes_n) {
    if (n <= 1) {
        return 0;
    }
    int i, sum;
    for (i = sum = 0; i != primes_n; i++) {
        int r = n - prime[i];
        if (r < 0) {
            break;
        } else if (r == 0) {
            sum++;
        } else {
            sum += primePartR(r, prime, i + 1);
        }
    }
    return sum;
}
/** dynamic programming with prime paration
 *  2d-ctx: n parition with max prime is p
 *  NMAX * n
 */
int primePart(int n, int **ctx, int *prime, int primes_n) {
    if (n <= 1) {
        return 0;
    }
    if (ctx[n] == NULL) {
        ctx[n] = malloc(sizeof(int) * primes_n);
        memset(ctx[n], 0, primes_n);
    } else {
        // printf("ctx n=%d primes_n=%d %d ret=%d\n", n, primes_n, prime[primes_n], ctx[n][primes_n]);
        return ctx[n][primes_n];
    }
    int i, sum;
    for (i = sum = 0; i != primes_n; i++) {
        int r = n - prime[i];
        if (r < 0) {
            break;
        } else if (r == 0) {
            sum += 1;
            ctx[n][i] = sum;
        } else {
            int d = primePart(r, ctx, prime, i);
            // printf("%d-%d %d\n", n, prime[i], d);
            sum += d;
            ctx[n][i] = sum;
        }
    }
    for (; i != primes_n; i++) {
        ctx[n][i] = sum;
    }
    // printf("n=%d primes_n=%d %d sum=%d\n", n, primes_n, prime[primes_n], sum);
    // show_int_arr(ctx[n], i, "ctx");
    return sum;
}

#define NMAX (300)
int main() {
    int primes_n;
    int *prime = primes(NMAX, &primes_n);
#if 0
    show_int_arr(prime, primes_n);
    return 0;
#endif
    int i, **ctx = malloc(sizeof(int *) * NMAX);
    for (i = 0; i != NMAX; i++) {
        ctx[i] = NULL;
    }
    for (i = 2; i != NMAX; i++) {
        int s = primePart(i, ctx, prime, primes_n);
        // int s = primePartR(i, prime, primes_n);
        printf("%d %d\n", i, s);
        if (s > 5000) {
            break;
        }
    }
    /** ans: 71 */
    for (i = 0; i != NMAX; i++) {
        if (ctx[i] != NULL) {
            free(ctx[i]);
        }
    }
    free(ctx);

    free(prime);
    return 0;
}
