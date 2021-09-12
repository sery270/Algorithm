#include <stdio.h>
#include <vector>
using namespace std;

int N, normal = 0, abnormal = 0;
bool twice = false;
char tmp;
bool visited[101][101];
bool visited2[101][101];
int g[101][101];
int dx[] = {-1, 1,0,0};
int dy[] = {0,0,-1,1};

bool able(int x, int y){
    return x>0 && x<=N && y>0 && y<=N? true: false;
}


void dfs(int x, int y){
    visited[x][y] = true;
    
    
    
    for(int i = 0 ;i <4; i++){
        if(!visited[x+dx[i]][y+dy[i]] && able(x+dx[i], y+dy[i])){
            if(g[x][y] == g[x+dx[i]][y+dy[i]]){
//                printf("%d\n",9);
                dfs(x+dx[i],y+dy[i]);
            }
        }
        
    }
    
}

void dfs2(int x, int y){
    visited2[x][y] = true;
    for(int i = 0 ;i <4; i++){
        if(!visited2[x+dx[i]][y+dy[i]] && able(x+dx[i], y+dy[i])){
            if(g[x][y] == g[x+dx[i]][y+dy[i]]){
//                printf("visited2 :: %d %d\n", x+dx[i],y+dy[i]);
                dfs2(x+dx[i],y+dy[i]);
            }
            if((g[x][y] == 0 && g[x+dx[i]][y+dy[i]] == 1) || (g[x][y] == 1 && g[x+dx[i]][y+dy[i]] == 0)){
//                if(!twice){
//                    twice = true;
//                    printf("R&G :: %d %d\n", x+dx[i],y+dy[i]);
                    dfs2(x+dx[i],y+dy[i]);
//                }
            }
        }
        
    }
    
}


int main(){
    scanf("%d", &N);
    for(int i = 1; i<=N; i++){
        for(int j = 1; j<=N; j++){
            scanf("%1s", &tmp);
            if(tmp == 'R'){
                g[i][j] = 0;
            }
            if(tmp == 'B'){
                g[i][j] = 2;
            }
            if(tmp == 'G'){
                g[i][j] = 1;
            }
        }
    }
    
    for(int i = 1; i<=N; i++){
        for(int j = 1; j<=N; j++){
            if(!visited[i][j]){
                dfs(i, j);
                normal++;
            }
            
            if(!visited2[i][j]){
//                printf("dfs2 :: %d %d\n", i,j );
//                twice = false;
                dfs2(i, j);
                
                abnormal++;
            }
            
            
        }
        
    }
    
    printf("%d %d", normal, abnormal);
    
    return 0;
}
