#include <cstdio>
#include <vector>
using namespace std;

int N, S, sum = 0, sol = 0;
vector<int> list(20);



int main(){
    scanf("%d %d", &N, &S);
    for(int i = 0; i<N; i++){
        scanf("%d", &list[i]);
    }
    
    
    for(int s = 1; s< (1<<N); s++){
        sum =0;
        for(int i = 0; i<N ; i++){
            if(s&(1<<i)){
                sum += list[i];
            }
        }
        
        
        if(sum == S){
            sol++;
        }
        
    }
    
    printf("%d", sol);
    
    return 0;
}

