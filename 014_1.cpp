#include <stdio.h>
#include <assert.h>

inline int cntColltz(unsigned long long n)
{
    int cnt = 0;
    while(n != 1){
        cnt++;
        if(n % 2 == 0){
            n = n >> 1;
        }else{
            n = 3 * n + 1;
        }
    }
    return cnt;
}

int main(){
    int m = 0;
    int mv = -1;
    int t;

    unsigned long long thres = 1000*1000;
    for(unsigned long long i = thres >> 2; i <= thres; i++){
        t = cntColltz(i);
        if(t > m){
            m = t;
            mv = i;
        }
    }
    printf("%d %d\n",mv,m);
    return 0;
}
