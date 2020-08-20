#include <cstdio>
#include <vector>
using namespace std;

vector<int> mem(11);
int N, T, sol;

//top-down
int dp(int n){
    if(mem[n] > 0){
    return mem[n];
    }else{
    mem[n] = dp(n-1) + dp(n-2) + dp(n-3);
    }
return mem[n];

}


int main(){
    mem[0] = 1;
    mem[1] = 1;
    mem[2] = 2;
    

    scanf("%d", &T);

    for(int i =0 ; i<T; i++){
        scanf("%d", &N);

        if(N == 1){
            sol = 1;
        }else if(N == 2){
            sol = 2;
        }else{
            sol = dp(N);
        }
        printf("%d\n", sol);
    }

    return 0; 
}