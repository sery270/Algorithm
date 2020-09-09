#include <iostream>
#include <vector>
using namespace std;

vector<int> mem;
int N;

int main(){
    cin >> N;
    mem.resize(N+1);
    mem[0] = 0;
    mem[1] = 1;
    mem[2] = 2;
    
    for(int i = 3; i<=N; i++){
        mem[i] = (mem[i-1] + mem[i-2])%15746;
    }
    cout << mem[N]%15746 << endl;
    return 0;
}

