#include <iostream>
#include <vector>
using namespace std;

vector<long long> mem;
int T, N;

int main(){
    cin >> T;

    while(T--){
        cin >> N;
        mem.resize(N+1);
        mem[1] = 1;         mem[2] = 1;        mem[3] = 1;

        for(int i = 4; i<=N;i++){
            mem[i] = mem[i-2] + mem[i-3];
        }


        cout << mem[N] << endl;

    }




    return 0;
}
