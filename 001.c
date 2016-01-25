/*
 * Kenneth E. Iverson's APL style
 * Ref: Concrete Math Ch2 SUMS 2.1 NOTATIONS Page24
 */
#include <stdio.h>

int main() {
    int i, sum;
    for (i = 0, sum = 0; i != 1000; i++) {
        // sum on a_k [P(k)]
        // [P(k)] = 1 if p has property
        // [p(k)] = 0 if p has NOT property
        sum += (i % 3 == 0 || i % 5 == 0) * i;
    }
    printf("%d\n", sum);
    return 0;
}
