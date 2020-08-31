#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int> a;
vector<int> mem;
int N;

int main(){
    cin >> N;
    a.resize(N);
    mem.resize(N);
    
    for(int i =0; i<N; i++){
        cin >> a[i];
    }

    mem[0] = a[0];
    for(int i =1; i<N; i++){
        if (mem[i-1] > 0){
           mem[i] = mem[i-1] + a[i];
        }else{
            mem[i] = a[i];
        }
    }

    sort(mem.begin(), mem.end());

    cout << mem[N-1] << endl;
    return 0;
}
