#include <stdio.h>

int sgcd(int x, int y)
{
    int cnt = 0;
    int t;
    while(1){
        t = x;
        x = y;
        y = t % y;
        cnt++;
        if(y == 0)
            return cnt;
    }
}


int Sgcd(int n)
{
    int cnt = 0,i,j;
    for(i = 1; i <= n; i++){
        printf("\r%16d %16d",i,cnt);
        cnt ++;
        for(j = 1; j < i; j++){
            cnt += 2 * sgcd(i, j) + 1;
        }
    }
    return cnt;
}

void main(){
    printf("\n");
    printf("\n%d\n",Sgcd(1000*1000));
}
