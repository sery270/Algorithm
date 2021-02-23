#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<int> D;

int dp(int now){
    if(D[now] > 0){
        return D[now];
    }
    D[now] = (2*dp(now-1) + dp(now-2))%9901;
    return D[now]%9901;
}

int main(){
    scanf("%d", &N);
    D.resize(N+1);
    D[0] = 1;
    D[1] = 3;
    
    printf("%d",dp(N)%9901);
    
    return 0;
}
