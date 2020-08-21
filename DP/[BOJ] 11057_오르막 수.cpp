#include <vector>
#include <cstdio>
using namespace std;

vector<vector<long long>> mem(1001, vector<long long>(10));
int N;
int sol = 0;


int main(){
    scanf("%d", &N);
    for(int i =0; i<10; i++){
        mem[1][i] = 1;
    }

    for(int i = 2; i <= N; i++){
        for(int end = 0; end < 10; end++){
            for(int j = end; j < 10; j++){
                mem[i][end] += mem[i-1][j];
                mem[i][end] %= 10007;
            }
        }
    }

    for(int i =0; i< 10; i++){
        sol += mem[N][i];
    }

    printf("%d", sol % 10007);
    return 0;
}
