#include <cstdio>
#include <vector>
using namespace std;

int T, n;



int main(){
    scanf("%d", &T);
    while(T--){
        scanf("%d", &n);
        vector<int> D(n+1);
        D[0] = 1;
        
        for(int i = 1; i<= 3; i++){
            for(int j = 1; j<=n; j++){
                if(j-i>=0){
                    D[j] += D[j-i];
                }
            }
        }
        
        printf("%d\n", D[n]);
                                  
        
    }
    return 0;
}
