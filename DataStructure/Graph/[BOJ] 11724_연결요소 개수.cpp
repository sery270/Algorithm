#include <stdio.h>
#include <vector>
using namespace std;

vector<int> g[1001];
//vector<int> visited;

int visited[1001];

int N, M;
int cnt = 0;
int a,b;


void dfs(int x){
    visited[x] = 1;
    
    for(int i = 0; i< g[x].size(); i++){
        if(g[x][i] != 0 && visited[g[x][i]] == 0){
            dfs(g[x][i]);
        }
        
    }
    
}

int main(){
    scanf("%d %d", &N, &M);
//    g.resize(N+1, vector<int>());
//    visited.resize(N+1);
    
    for(int i =0; i<M; i++){
        scanf("%d %d", &a, &b);
        g[a].push_back(b);
        g[b].push_back(a);
    }
    
    for(int i =1; i<= N; i++){
        if(visited[i] == 0){
            cnt++;
            dfs(i);
        }
       
    }
    
    printf("%d\n", cnt);
    return 0;
}
