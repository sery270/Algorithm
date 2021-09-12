#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
using namespace std;

int R, C , sol=1, cnt =1;
char tmp;
int g[21][21];
bool visited[21][21];
bool alpha[100];
int dx[4] = {-1, 1, 0,0}, dy[4] = {0,0,-1,1};

bool able(int x, int y){
    return x>0 && x<=R && y>0&& y<=C;
}

void dfs(int x, int y){
    visited[x][y] = true;
    alpha[g[x][y]] = true;
    for(int i =0; i<4; i++){
        
        if(!visited[x+dx[i]][y+dy[i]] && able(x+dx[i], y+dy[i])){
//            printf("%d %d\n", g[x+dx[i]][y+dy[i]], g[x][y]);
            if(!alpha[g[x+dx[i]][y+dy[i]]]){
                cnt++;
//                printf("%d %c %c \n", cnt, (char)g[x][y],(char)g[x+dx[i]][y+dy[i]]);
                sol = sol<cnt? cnt: sol;
                dfs(x+dx[i], y+dy[i]);
                
                cnt--;
                visited[x+dx[i]][y+dy[i]] = false;
                alpha[g[x+dx[i]][y+dy[i]]] = false;
                
            
            }
        }
    }
    
    
}

int main(){
    scanf("%d %d", &R, &C);
    
    for(int i =1; i<= R; i++){
        for(int j = 1; j<=C; j++){
            scanf("%1s", &tmp);
            g[i][j] = (int)tmp;
//            printf("%d ",g[i][j]);
            
        }
    }
    
//    for(int i =1; i<= R; i++){
//        for(int j = 1; j<=C; j++){
//            if(!visited[i][j]){
//                cnt = 0;
//                dfs(i, j);
//                sol = sol<cnt? cnt: sol;
//            }
//        }
//    }
    
//    for(int i =0; i<4; i++){
//        cnt = 1;
//        memset(alpha, false, 100);
//        for(int i =1; i<= R; i++){
//            for(int j = 1; j<=C; j++){
//                visited[i][j] = false;
//            }
//        }
//        visited[1][1] = true;
//        alpha[g[1][1]] = true;
//        if(!visited[1+dx[i]][1+dy[i]] && able(1+dx[i], 1+dy[i])){
////            printf("%d %d", g[x+dx[i]][y+dy[i]], g[x][y]);
//            if(!alpha[g[1+dx[i]][1+dy[i]]]){
//                cnt++;
////                printf("%d %d %d \n", cnt, g[x+dx[i]][y+dy[i]], g[x][y]);
//                dfs(1+dx[i], 1+dy[i]);
//            }
//        }
//        sol = sol<cnt? cnt: sol;
//    }
    
    dfs(1,1);

    
    printf("%d", sol);
    
    
    return 0;
}
