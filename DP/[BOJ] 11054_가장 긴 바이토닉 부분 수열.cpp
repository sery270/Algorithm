#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> a;
vector<int> ra;
vector<int> mem(1001);
vector<int> rmem(1001);
int N;

int main(){
    cin >> N;
    a.resize(N+1);
    ra.resize(N+1);
    for(int i =1; i<=N ;i ++){
        cin >> a[i];
        ra[N-i+1] = a[i];
    }
    
    for(int now = 1; now<=N; now++){
        mem[now] = 1;
        for(int i =1; i<now; i++){
            if(a[i] < a[now] && mem[now] < mem[i] + 1){
                mem[now] = mem[i] + 1;
            }
            if(ra[i] < ra[now] && rmem[now] < rmem[i] + 1){
                rmem[now] = rmem[i] + 1;
            }
        }
        
        //cout << now << "   mem[now]: " << mem[now] << "||" << N-now+1<<"  rmem[now]: " << rmem[now] << endl;
    }
    
    for(int i =1; i<=N; i++){
        mem[i] += rmem[N-i+1];
    }

    sort(mem.begin(), mem.end());
    cout << mem[1000]<< endl;
    return 0;
}

