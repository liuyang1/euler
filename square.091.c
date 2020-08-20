#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x, y;
} Point;

static inline Point vec(Point a, Point b) {
    Point c = {.x = a.x - b.x, .y = a.y - b.y};
    return c;
}

static inline int norm2(Point a) {
    return a.x * a.x + a.y * a.y;
}

bool isRight(Point a, Point b) {
    int n0 = norm2(a), n1 = norm2(b), n2 = norm2(vec(a, b));
    if (n0 > n1 && n0 > n2) {
        return n0 == n1 + n2;
    }
    if (n1 > n0 && n1 > n2) {
        return n1 == n0 + n2;
    }
    if (n2 > n0 && n2 > n0) {
        return n2 == n0 + n1;
    }
    return false;
}

Point *grid(int n, int m) {
    Point *xs = malloc(sizeof(Point) * n * m);
    int i, j, k;
    for (i = k = 0; i != n; i++) {
        for (j = 0; j != m; j++) {
            Point a = {.x = i, .y = j};
            xs[k++] = a;
        }
    }
    return xs;
}

size_t rightTri(int n, int m) {
    Point *pts = grid(n, m), *c = pts + 1; /** skip first (0,0) */
    int sz = n * m - 1;
    int i, j, cnt;
    for (i = cnt = 0; i != sz; i++) {
        for (j = i + 1; j != sz; j++) {
            cnt += isRight(c[i], c[j]);
        }
    }
    free(pts);
    return cnt;
}

int main() {
    int i;
    for (i = 1; i != 51; i++) {
        printf("%d %zu\n", i, rightTri(i + 1, i + 1));
    }
    return 0;
}
