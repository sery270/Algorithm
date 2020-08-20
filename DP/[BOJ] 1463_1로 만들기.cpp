#include <cstdio>
#include <vector>
using namespace std;

vector<int> mem(1000000);
int N;

//top-down
int dp(int n){
    if(n == 1){return 0;}
    if(mem[n] > 0){return mem[n];}
    
    mem[n] = dp(n-1) + 1;
    if(n % 2 == 0){
        if(mem[n/2] > 0){
            mem[n] = mem[n/2] + 1 > mem[n] ? mem[n] : mem[n/2] + 1;
        }else{
            dp(n/2);
            mem[n] = mem[n/2] + 1 > mem[n] ? mem[n] : mem[n/2] + 1;
        }
    }
    if(n % 3 == 0){
        if(mem[n/3] > 0){
            mem[n] = mem[n/3] + 1 > mem[n] ? mem[n] : mem[n/3] + 1;
        }else{
            dp(n/3);
            mem[n] = mem[n/3] + 1 > mem[n] ? mem[n] : mem[n/3] + 1;
        }
    }
    return dp(n);
}

int main(){
    scanf("%d", &N);
    int sol = dp(N);
    printf("%d", sol);
    return 0;
}
