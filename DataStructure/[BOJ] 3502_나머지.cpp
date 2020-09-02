#include <iostream>
#include <vector>
using namespace std;

vector<int> a(10);
vector<int> m(42);
int cnt = 0;

int main(){
    for(int i=0;i<10;i++){
        cin >> a[i];
        m[a[i]%42]++;
    }
    
    for(int i=0;i<42;i++){
        if(m[i] != 0){
            cnt++;
        }
    }

    cout << cnt << endl;
    return 0;
}
