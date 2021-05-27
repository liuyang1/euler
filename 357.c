/** project euler 357 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

void sieve(char *a, int n) {
	memset(a, 1, n);
	a[0] = a[1] = 0;
	int i, j;
	for (i = 2; i * i < n; i++) {
		if (a[i] == 0) {
			continue;
		}
		for (j = 2 * i; j < n; j += i) {
			a[j] = 0;
		}
	}
#if 0
	for (i = 0; i != n; i++) {
		if (a[i]) {
			printf("%d\n", i);
		}
	}
#endif
}

static inline int cond(int n, char *primes) {
	int j;
	for (j = 1; j * j <= n; j++) {
		if (n % j == 0) {
			int x = j + n / j;
			if (!primes[x]) {
				return 0;
			}
		}
	}
	return 1;
}

int main() {
	// int n = 100;
	int n = 1000 * 1000 * 100;
	char *a = malloc(sizeof(char) * n);
	sieve(a, n);

	uint64_t sum = 0;
	int i, j;
	for (i = 1; i != n; i++) {
		// only prime=2 match COND
		// check all primes here
		if (cond(i, a)) {
			sum += i;
			// printf("%d %"PRIu64"\n", i, sum);
		}
	}
	printf("%"PRIu64"\n", sum);
	free(a);
	return 0;
}
