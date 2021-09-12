#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> g;
vector<int> cnt;
int dx[4] = {-1,1,0,0};
int dy[4] = {0,0,-1,1};
int T, Dcnt;




//
//bool able(){
//
//    return true;
//}
void dfs(int x , int y){
    if(g[x][y] == 0){
        return;
    }
    
    g[x][y] = 0;
    for(int i = 0; i<4; i++){
        if(g[x+dx[i]][y+dy[i]]==1){
            cnt[Dcnt]++;
            dfs(x+dx[i], y+dy[i]);
        }
    }
    
}



int main(){
    scanf("%d",&T);
    g.resize(T+2, vector<int>(T+2));
    Dcnt = 0;
    
    for(int i = 1; i<=T;i++){
        for(int j = 1; j<=T;j++){
            scanf("%1d", &g[i][j]);
        }
    }
    
    
    
    for(int i = 1; i<=T;i++){
        for(int j = 1; j<=T;j++){
            if(g[i][j] == 1){
                cnt.push_back(1);
                dfs(i,j);
                Dcnt++;
            }
        }
    }
    
    
    sort(cnt.begin(), cnt.end());
    printf("%d\n", Dcnt);
    for(int i = 0; i<cnt.size();i++){
        printf("%d\n", cnt[i]);
    }
    return 0;
}
