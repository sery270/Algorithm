#include <stdio.h>
#include <vector>
using namespace std;

int T, n, a, point, cnt;
vector<int> g(100001);
vector<bool> visited(100001);
vector<bool> tmp;

void dfs(int x){
    visited[x] = true;
    tmp[x] = true;
    
    
    
    
    if(x == g[x]){
        return;
    }else{
        if(g[x] == point){
            for(int i =1; i<=n; i++){
                if(tmp[i]){
//                    printf("point : %d i : %d x: %d\n", point, i, x);
                    cnt++;
                }
            }
            return;
        }else{
            if(!visited[g[x]]){
//                printf("\ndfs %d", g[x]);
                dfs(g[x]);
            }
            
        }

}
}



int main(){
    
    scanf("%d", &T);

    while(T--){
        g = vector<int>(100001);
        visited = vector<bool>(100001);
        tmp = vector<bool>(100001);
        cnt = 0;
        
        scanf("%d", &n);
        for(int i = 1; i<=n ; i++){
            scanf("%d", &g[i]);
            if(i == g[i]){
                visited[i] = true;
                cnt++;
            }
        }
        
        for(int i =1; i<=n ;i++){
            if(!visited[i]){
                point = i;
                tmp = vector<bool>(100001);
                dfs(i);
            }
            
        }

        
        printf("%d\n",n-cnt);
    }
    
    
    
    
    return 0;
}
