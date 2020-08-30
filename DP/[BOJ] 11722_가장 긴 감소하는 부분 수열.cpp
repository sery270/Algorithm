#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> a(1001);
vector<int> mem(1001);
int N;

int main(){
    cin >> N;
    for(int i = 1; i<=N ; i++){
        cin >> a[i];
    }

    for(int now =1; now<=N; now++){
        mem[now] = 1;
        for(int i = 0; i<now; i++){
            if(a[i]> a[now] && mem[i]+1 > mem[now]){
                mem[now] = mem[i]+1;
            }
        }
    }

    sort(mem.begin(), mem.end());
    cout << mem[1000] << endl;

    return 0;
}
