#include <iostream>
#include <vector>
using namespace std;

long long T, N, sol;
vector<long long> a;

long long GCD(long long a, long long b){
    if(b == 0){
        return a;
    }else{
        return GCD(b, a%b);
    }
}

int main(){
    cin >> T;
    while(T--){
        cin >> N;
        a.resize(N+1);
        sol = 0;
        for(int i = 1; i<=N; i++){
            cin >> a[i];
        }
        
        for(int i = 1; i<N; i++){
            for(int j = i+1; j<=N; j++){
                sol += GCD(a[i],a[j]);
            }
        }
        cout << sol <<  endl;
    }
    
    
    
    
    return 0;
}
