#include <cstdio>
#include <vector>
using namespace std;

long long max(long long a,long long b){
    return a>b?a:b ;
} 

vector<vector<long long>> a;
vector<vector<long long>> mem;

int main(){
    int T, N;
    scanf("%d", &T);

    while ((T--))
    {
        scanf("%d", &N);
        a.resize(N+1, vector<long long> (3));
        mem.resize(N+1, vector<long long> (3));
        for(int i =1 ; i<=N; i++){
            scanf("%lld", &a[i][1]);
        }
        for(int i =1 ; i<=N; i++){
            scanf("%lld", &a[i][2]);   
        }
        for(int i =1; i<=N ; i++){
            mem[i][0] = max(mem[i-1][0], max(mem[i-1][1], mem[i-1][2]));
            mem[i][1] = max(mem[i-1][0], mem[i-1][2]) + a[i][1];
            mem[i][2] = max(mem[i-1][0], mem[i-1][1]) + a[i][2];
        }
        long long sol = 0;
        for(int i = 1; i<=N; i++){
            sol = max(max(sol,mem[i][0]), max(mem[i][1], mem[i][2]));
        }

        printf("%lld\n",sol);        
    }
    

    return 0;
}