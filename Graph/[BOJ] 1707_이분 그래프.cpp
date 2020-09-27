#include <cstdio>
#include <string.h>
#include <stdio.h>
#include <vector>
using namespace std;
int T, V, E, a, b;
bool sol = true;

vector<int> g[20001];
int visited[20001];



void dfs(int node, int c) {
    visited[node] = c;
    for (int i=0; i<g[node].size(); i++) {
        if (visited[g[node][i]] == 0) {
            dfs(g[node][i], 3-c);
        }
    }
}
int main(){
    scanf("%d", &T);
    
    
    while(T--){
        
        scanf("%d %d", &V, &E);
        for (int i=1; i<=V; i++) {
            g[i].clear();
            visited[i] = 0;
        }
        sol = true;
//        memset(visited, 0, 20001);
        
        for(int i =0; i<E; i++){
            scanf("%d %d", &a, &b);
            g[a].push_back(b);
            g[b].push_back(a);
        }
        
        for(int i = 1; i<=V; i++){
            if(visited[i] == 0){
                dfs(i,1);
            }
        }
        
        for(int i = 1; i<=V; i++){
            for(int j = 0; j<g[i].size();j++){
                if(visited[i] == visited[g[i][j]]){
                    sol = false;
                }
            }
        }

        if(sol){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
        
    }
    
    
    return 0;
}
