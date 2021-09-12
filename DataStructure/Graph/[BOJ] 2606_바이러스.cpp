#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int g[101][101] = {0};
int visit[101] = {0};

//시작 정점와 정점 개수
void DFS(int v, int n){
    visit[v] = 1;
    
    for(int i =1; i <= n; i++){
        if(g[v][i] == 1 && visit[i] == 0){
            DFS(i, n);
        }
    }
    
    
}

int main() {
    
    int N, M; // 노드와 간선 개수
    cin >> N >> M;
 
    int x,y;
    
    for(int i = 1; i <= M; i++){
        cin >> x >> y;
        g[x][y] = 1;
        g[y][x] = 1;
    }
    
    DFS(1, N);
    
    int cnt = 0;
    
    for(int i =1; i<= N; i++){
        if(visit[i] == 1){
            cnt++;
        }
    }
    
    cout << cnt-1 << endl;
    
    return 0;
}