#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

int maxH = 0, N, cnt =0, maxcnt = 1, nowH;
bool visted[101][101];
int g[101][101];
int dx[4] = {-1, 1, 0,0}, dy[4] = {0,0,-1,1};


bool able(int x, int y){
    
    
    return x<=N && x>0 && y>0 && y<=N? true: false;
}

void dfs(int x, int y){
    visted[x][y] = true;
    
    for(int i =0; i<4; i++){
        if(able(x+dx[i], y+dy[i]) && !visted[x+dx[i]][ y+dy[i]]){
            if(g[x+dx[i]][y+dy[i]] > nowH){
                dfs(x+dx[i], y+dy[i]);
            }
        }
    }
    
    
    
    
    
}


int main(){
    scanf("%d", &N);
    
    for(int i = 1; i <= N ; i++){
        for(int j = 1; j <= N; j++){
            scanf("%d", &g[i][j]);
            if(maxH < g[i][j]) maxH = g[i][j];
        }
    }
    
    for(int h = 0; h <= maxH-1; h++){
        for (int i = 0; i <= N; i++){
            for (int j = 0; j <= N; j++){
                visted[i][j] = false;
            }
        }
        nowH = h;
        cnt = 0;
        for(int i = 1; i <= N ; i++){
            for(int j = 1; j <= N; j++){
                if(!visted[i][j] && g[i][j] > nowH){
                    dfs(i, j);
                    cnt++;
                }
            }
        }
//        printf("%d\n" , cnt);
        if(maxcnt < cnt) maxcnt = cnt;
        
    }
    
    printf("%d\n", maxcnt);

    return 0;
}
