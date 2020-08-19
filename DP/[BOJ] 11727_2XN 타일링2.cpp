#include <cstdio>
#include <vector>
using namespace std;

vector<long long> mem(1001);
int N;

long long dp(int n){
    if(mem[n] > 0){
        return mem[n];
    }else{
        mem[n] = (dp(n-1) + 2 * dp(n-2)) % 10007; 
    }

    return mem[n];
}

int main(){
    int sol;
    mem[0] = 1;
    mem[1] = 1;
    scanf("%d", &N);

    if(N == 1){
        sol = 1;
    }
    if(N > 1){
        sol = dp(N);
    }

    printf("%d", sol%10007);


    return 0;
}
