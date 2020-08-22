#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/** https://projecteuler.net/problem=104
 * Fibonacci sequence
 * the first number which first 9 digits & last digits is pandigital
 */
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))


char *add(char *xs, int n, char *ys, int m, int *out_l) {
    int l = MAX(n, m);
    int nm = MIN(n, m);
    char *zs = malloc(sizeof(char) * (l + 1));
    int i, c;
    for (i = c = 0; i < nm; i++) {
        c += xs[i] + ys[i], zs[i] = c % 10, c /= 10;
    }
    for (; i < n; i++) {
        c += xs[i], zs[i] = c % 10, c /= 10;
    }
    for (; i < m; i++) {
        c += ys[i], zs[i] = c % 10, c /= 10;
    }
    zs[i] = c;
    *out_l = c == 0 ? l : l + 1;
    return zs;
}
void show(char *xs, int n) {
    for (int i = 0; i != n; i++) {
        printf("%d", xs[i]);
    }
    printf("\n");
}

#define DIGIT_N     9
bool isPand(char *xs, int len) {
    if (len < DIGIT_N) {
        return false;
    }
    // show(xs, len);
    char d[DIGIT_N + 1];
    memset(d, 0, DIGIT_N + 1);
    int i;
    for (i = 0; i != DIGIT_N; i++) {
        int idx = xs[i];
        d[idx]++;
        if (d[idx] > 1 || d[0] == 1) {
            return false;
        }
    }
    // show(d, DIGIT_N);
    return true; // Pand is [1..9], without 0
}

int main() {
    char *f0 = malloc(sizeof(char) * 1), *f1 = malloc(sizeof(char) * 1);
    char *f2 = NULL;
    int n0 = 1, n1 = 1, n2;
    f0[0] = 1, f1[0] = 1;
    int i;
    for (i = 0; i != 3000; i++) {
        f2 = add(f0, n0, f1, n1, &n2);
        // printf("%d ", i + 3), show(f2, n2);
        bool cond1 = isPand(f2, n2);
        bool cond2 = false;
        if (n2 >= 9) {
            cond2 = isPand(f2 + n2 - 9, 9);
        }
        if (cond1 && cond2) {
            printf("%d ", i + 3), show(f2, n2);
            break;
        }
        free(f0), f0 = f1, f1 = f2, n0 = n1, n1 = n2, f2 = NULL;
    }
    /** ans: 329468, cost 59s */
    free(f0), free(f1);
    if (f2) {
        free(f2);
    }
    return 0;
}
