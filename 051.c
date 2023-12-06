#include <stdint.h>
#include <stdio.h>
#include <stdbool.h>

bool isprime(uint32_t x) {
    if (x == 0 || x == 1) {
        return false;
    }
    if (x == 2) {
        return true;
    }
    if (x % 2 == 0) {
        return false;
    }
    uint32_t i;
    for (i = 3; i * i <= x; i += 2) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    uint32_t i;
    uint32_t low = 1000 * 10000;
    uint32_t high = low * 10;
    for (i = low + 1; i != high; i++) {
        if (isprime(i)) {
            printf("%d\n", i);
        }
    }
    return 0;
}
