#include <cstdio>
#include <vector>
using namespace std;

vector<long long> mem(1001);

int N;
long long sol;

//top-down
long long dp(int n){
//    int m1, m2;
    if(mem[n] > 0){ // 값이 있을 때
        return mem[n];
    }else{
        mem[n] = dp(n-2)%10007 + dp(n-1)%10007;
    }
    
    return mem[n];
}

int main(){
    scanf("%d",&N);
    mem[0] = 1;
    mem[1] = 1;
    mem[2] = 2;
    if(N == 1){
        sol = 1;
    }else if(N == 2){
        sol = 2;
    }else{
        sol = dp(N);
    }
    //int s = sol;
    printf("%d",sol % 10007);
    
    
    
    
    return 0;
}

