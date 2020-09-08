#include <iostream>
#include <vector>
using namespace std;
vector<char> sol;
vector<char> list(35);

int main(){
    int N, B;
    cin >> N >> B;
    
    for(int i = 0; i<=9; i++){
        list[i] = i+48;
    }
    
    for(int i = 10; i<=35; i++){
        list[i] = char(i+55);
    }
    int cnt = 0;
    while(N>0){
        sol.push_back(list[N%B]);
        N=int(N/B);
        cnt++;
    }
     sol.push_back(N);
    for(int i = cnt-1; i>=0 ;i--){
        cout << sol[i];
    }
    
    return 0;
}
