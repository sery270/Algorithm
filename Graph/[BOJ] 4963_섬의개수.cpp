#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g(52, vector<int>(52)); //51까지 하면 되는데, +1 할거 생각하면 52까지!
int dx[8] = {0,0,-1,1,1,-1,-1,1};
int dy[8] = {-1,1,0,0,-1,1,-1,1};
int W, H, tmp;
int cnt = 0;

// 배열을 함수의 인자로 주고 받는것은 메모리든 시간이든 매우 비효율 적이다. 
// 전역 배열을 선언하는 것이 PS에선 좋겠다. 

// void dfs(vector<vector<int>> tmp, int x, int y){
//     if(tmp[x][y] == 0){
//         return;
//     }
    
//     g[x][y] = 0;
    
//     for (int i =0; i < 8; i++) {
//         dfs(g, x+dx[i], y+dy[i]);
//          //cout << "dfs>>>" << i << "x: " << x << "y: " << y << endl;
//     }
// }

void dfs(int x, int y){
    if(g[x][y] == 0){
        return;
    }

    g[x][y] = 0;
    
    for (int i =0; i < 8; i++) {
        //이렇게 재귀 호출이 필요한 경우를 필터링 해주는 것은 시간적으로 많이 절약된다. 
        //메모리는 큰 상관이 없다.
        if(g[x+dx[i]][y+dy[i]] == 1){
            dfs(x+dx[i], y+dy[i]);
        }
         //cout << "dfs>>>" << i << "x: " << x << "y: " << y << endl;
    }
}



//딱히 지도 초기화 필요가 없는게, 어차피 다 0으로 만들거임
int main(){
    
    cin >> W >> H;
    while(W != 0 && H != 0){
        
        cnt = 0;
        //resize는 시간이든, 메모리든 큰 영향이 없다.
        g.resize(52,vector<int>(52));
        for(int i = 1; i<= H; i++){
            for(int j = 1; j<= W; j++){
                cin >> tmp;
                g[i][j] = tmp;
            }
        }
        for(int i = 1; i<= H; i++){
            for(int j = 1; j<= W; j++){
                if(g[i][j] == 1){
                    //cout << "x: " << i << "y: " << j << endl;
                    //dfs(g, i, j);
                    dfs(i, j);
                    cnt++;
                }
            }
        }
        cout << cnt << endl;
        cin >> W >> H;
    }
    
    
    
    return 0;
}
