#include <iostream>
#include <vector>
using namespace std;

vector<int> a(10001);
vector<vector<int>> mem(10001, vector<int>(3));
int N;

int max(int a,int b){
    return a>b?a:b;
}

int main(){
    cin >> N;
    for(int i =1; i<=N; i++){
        cin >> a[i];
    }
    mem[1][0] = 0;
    mem[1][1] = a[1];
    mem[1][2] = a[1];
    mem[2][0] = mem[1][0] + mem[1][1];
    mem[2][1] = a[2];
    mem[2][2] = a[1] + a[2];
    
    
    for(int i =3; i<=N; i++){
        mem[i][0] = max(mem[i-1][0], max( mem[i-2][0] + a[i-1], mem[i-2][1] + a[i-1]) );
        mem[i][1] = mem[i-1][0] + a[i];
        mem[i][2] = mem[i-2][0] + a[i] + a[i-1];
    }
    
    cout << max(mem[N][0], max(mem[N][1], mem[N][2])) << endl;
    return 0;
}
