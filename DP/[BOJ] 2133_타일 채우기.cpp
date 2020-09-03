#include <iostream>
#include <vector>
using namespace std;

vector<int> mem(31);
int N;

int main(){
    cin >> N;

    mem[0] = 1;
    mem[1] = 0;

    for(int i= 2; i<=N; i=i+2){
        mem[i] = mem[i-2] * 3;
        for(int j = 2; 2*j <= i; j++){
            mem[i] += mem[i-j*2] * 2;
        }
    }


    cout << mem[N] << endl;

}
