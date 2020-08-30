#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> mem(1001);
vector<int> a(1001);
int N;

int main(){
    cin >> N;
    for(int i = 1; i<=N; i++){
        cin >> a[i];
    }

    for(int now = 1; now <=N; now++){
        mem[now] = a[now];
        for(int j = 1; j < now; j++){
            if(a[j] < a[now] && mem[j] + a[now] > mem[now]){
                mem[now] = mem[j] + a[now];
             }
        }
    }

    sort(mem.begin(), mem.end());
    cout << mem[1000] << endl;




    return 0;
}
