#include <iostream>
using namespace std;

int main(){
    int N;
    cin >> N;
    
    for(int i = 1;i<=N; i++){
        for(int j = 0; j<N-i; j++){
            cout << " ";
        }
        for(int z = N-i; z<N; z++){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
