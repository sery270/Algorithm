#include <iostream>
#include <vector>
using namespace std;

int T, a,b, gcd;


int GCD(int a, int b)
{
    if(b == 0){
        return a;
    }else{
        return GCD(b, a%b);
    }
}
int main(){
    
    cin >> T;
    while(T--){
        cin >> a >> b;
        gcd = GCD(a,b);
        cout << a*b/gcd << endl;
    }


    return 0;
}
