#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> a(1001);
vector<int> mem;
int N;
int main(){
    cin >> N;
    mem.resize(N+1);
    for(int i =1; i<=N; i++){
        cin >> a[i];
    }
    for(int now =1; now<=N; now++){
        mem[now] = 1;
        for(int i= 1; i<now; i++){
            if(a[now]>a[i] && mem[i] + 1 > mem[now]){
                mem[now] = mem[i] + 1;
            }
        }
    }

    sort(mem.begin(), mem.end());
    
    cout << mem[N] << endl;
    return 0;
}
