#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
void showDigit8(uint8_t a[8], char e) {
    uint32_t i;
    printf("[");
    for (i = 0; i != 8; i++) {
        // printf("%d, ", a[i]);
        printf("%c, ", a[i]);
    }
    printf("]");
    if (e != 0) {
        printf("%c", e);
    }
}

void toDigit8(uint32_t x, uint8_t a[8]) {
    uint32_t i;
    for (i = 0; i != 8; i++) {
        a[i] = x % 10;
        x /= 10;
    }
    assert(x == 0);
}

bool sameWithMask(uint8_t a[8], uint8_t b[8], uint8_t m) {
    uint32_t i;
    for (i= 0; i != 8; i++) {
        if (m % 2 == 1) {
            if (a[i] != b[i]) {
                return false;
            }
        }
        m /= 2;
    }
    return true;
}

int test() {
    uint32_t a = 80000839;
    uint32_t b = 80000867;
    uint8_t ax[8], bx[8];
    toDigit8(a, ax);
    toDigit8(b, bx);
    showDigit8(ax, '\n');
    showDigit8(bx, '\n');

    uint8_t m;
    for (m = 0; m != 255; m++) {
        if (sameWithMask(ax, bx, m)) {
            printf("%x: ", m);
            showDigit8(ax, 0);
            showDigit8(bx, '\n');
        }
    }
    return 0;
}

typedef struct {
    uint8_t a[9];
} ent;

typedef struct {
    uint8_t b[32];  // 256
} bitarr;
int main() {
    FILE *fp = fopen("prime8.txt", "ro");
    ent *lst = malloc(sizeof(ent) * 5100000);
    uint32_t i;
    for (i = 0; !feof(fp); i++) {
        fgets(lst[i].a, 9, fp);
        fgetc(fp); // eat the newline
        // lst[i].a[8] = '\0'; // overflow
        // puts(lst[i]. a);
    }
    uint32_t len = i - 1;
    printf("cnt:%d\n", len);
    bitarr *flag = malloc(sizeof(bitarr) * len);
    memset(flag, 0, sizeof(bitarr) * len);
    uint8_t m;
    
    for (i = 0; i != 1000; i++) {
        printf("check on: ");
        showDigit8(lst[i]. a, '\n');
        for (m = 1; m != 255; m++) {
            uint32_t cnt = 0, j;
            for (j = i + 1; j != len; j++) {
#if 1
                if (sameWithMask(lst[i].a, lst[j].a, m)) {
                    printf("mask=%02x: ", m);
                    showDigit8(lst[i].a, '\0');
                    showDigit8(lst[j].a, '\n');
                }
#endif
                cnt += sameWithMask(lst[i].a, lst[j].a, m);
                if (cnt > 7) {
                    break;
                }
            }
            if (cnt == 7) {
                printf("mask=%x\n", m);
                showDigit8(lst[i].a, '\n');
                goto final;

            } else {
                printf("mask=%02x cnt=%d\n", m, cnt);
            }
        }
    }

final:

    free(flag);
    free(lst);
    fclose(fp);
    return 0;
}
