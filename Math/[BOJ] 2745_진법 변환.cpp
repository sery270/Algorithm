#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;
vector<int> list(100);


int main(){
    string N;
    int B;
    cin >> N >> B;
    
    for(int i = 0; i<=9; i++){
        list[i+48] = i;
    }
    
    for(int i = 10; i<=36; i++){
        list[i+55] = i;
    }
    
    int sol = 0;
    int cnt = 0;
    int size = int(N.length());
    
    for(int i = size-1; i>=0; i--){
        sol += list[int(N[i])] * pow(B, cnt);
        cnt++;
    }
    
    cout << sol ;

    return 0;
}
