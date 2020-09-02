#include <iostream>
#include <vector>
using namespace std;

vector<int> mem(100001);
int N, now;

int main(){
    cin >> N;

    mem[1] = 1;
    mem[2] = 2;
    for(int i = 2; i<=N; i++){
        mem[i] = i;
        for(int j = 1; i >= j*j; j++){
            if(mem[i] > mem[i-j*j] + 1){
                mem[i] = mem[i-j*j] + 1;
            }
        }
        //cout << i << ":  " << mem[i] << endl;
    }


    cout << mem[N] << endl;


    return 0;
}
