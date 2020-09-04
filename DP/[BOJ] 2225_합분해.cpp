#include <iostream>
#include <vector>
using namespace std;

vector<vector<long long>> mem(201,vector<long long>(201));
int N, K;

int main(){
    cin >> N >> K;

    mem[0][0] = 1;
    
    
    for(int k =1; k<=K; k++){
        for(int i = 0; i<=N; i++){
            for(int j = 0; j<=i; j++){
                mem[k][i] += mem[k-1][i-j];
                mem[k][i] %= 1000000000;
            }
        }
    }
    
    cout <<  mem[K][N] << endl;
    
    
    return 0;
}
