#include <cstdio>
#include <vector>
using namespace std;

vector<vector<long long >> mem(91,vector<long long >(2));
long long N, sol = 0;

int main(){
    mem[0][0] = 0;
    mem[0][1] = 0;
    mem[1][0] = 0;
    mem[1][1] = 1;
    mem[2][0] = 1;
    mem[2][1] = 0;
    
    scanf("%lld", &N);
    
    for(int n = 3;n <=N; n++){
        for(int i = 0; i<2; i++){
            if(i == 0 ){
                mem[n][i] += mem[n-1][0] + mem[n-1][1];
            }else if(i == 1 ){
                mem[n][i] += mem[n-1][0];
            }
            
        }
    }
    
    printf("%lld", mem[N][0] + mem[N][1]);
    
    return 0;
}
