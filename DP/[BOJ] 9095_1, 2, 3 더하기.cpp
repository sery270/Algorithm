#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int T, n;
vector<int> D;

int dp(int n){
    if (D[n] > 0){
        return D[n];
    }
    D[n] = dp(n-1) + dp(n-2) + dp(n-3);
    return D[n];
}


int main(){
    scanf("%d", &T);
    
    while(T--){
        scanf("%d", &n);
        D.resize(n+1);
        D[0] = 1;
        D[1] = 1;
        D[2] = 2;
        printf("%d\n", dp(n));
        
    }
    return 0;
}
