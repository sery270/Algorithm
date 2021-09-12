#include <stdio.h>
#include <vector>
#include <string.h>
using namespace std;


bool visited[1001] = {false,};
vector<int> g[1001];
int T,N, tmp;
int cnt =0 ;

void dfs(int x){
    if(visited[x]){
        cnt++;
        return;
    }
    
    visited[x] = true;
    
    for(int i =0; i<1; i++){
    
            dfs(g[x][i]);
        
    }
    
}


int main(){
    scanf("%d", &T);
    
    while(T--){
        cnt = 0;
//        memset(visited, false, 1001);
//        memset(g, 0, 1001); => 런타임에러
        
        scanf("%d", &N);
        for (int i=1; i<=N; i++) {
            g[i].clear();
            visited[i] = false;
        }
        
        for(int i =1; i <= N; i++){
            scanf("%d", &tmp);
            g[i].push_back(tmp);
        }
        for(int i =1; i <=N; i++){
            if(!visited[i]){
                dfs(i);
            }
        }
        
        printf("%d\n", cnt );
    }
    
    
    
    
    return 0;
}
