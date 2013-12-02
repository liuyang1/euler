#include <iostream>
#include <map>
using namespace std;

static map<int,int> ColltzMap;

int cntColltz(int n)
{
    if(ColltzMap.count(n))
        return ColltzMap[n];
    int v;
    if(n % 2 == 0)
        v = cntColltz(n >> 1) + 1;
    else
        v = cntColltz(n * 3 + 1) + 1;
    ColltzMap[n] = v;
    return v;
}
int main(){
    ColltzMap[1] = 0;
    cout<<cntColltz(13)<<endl;
    cout<<cntColltz(997823)<<endl;
    return 0;
}
