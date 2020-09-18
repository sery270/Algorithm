#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> g(52, vector<int>(52)); //51까지 하면 되는데, +1 할거 생각하면 52까지!
int dx[8] = {0,0,-1,1,1,-1,-1,1};
int dy[8] = {-1,1,0,0,-1,1,-1,1};
int W, H, tmp;
int cnt = 0;

void dfs(vector<vector<int>> tmp, int x, int y){
    if(tmp[x][y] == 0){
        return;
    }
    
    g[x][y] = 0;
    
    for (int i =0; i < 8; i++) {
        dfs(g, x+dx[i], y+dy[i]);
         //cout << "dfs>>>" << i << "x: " << x << "y: " << y << endl;
    }
}



//딱히 지도 초기화 필요가 없는게, 어차피 다 0으로 만들거임
int main(){
    
    cin >> W >> H;
    while(W != 0 && H != 0){
        
        cnt = 0;
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
                    dfs(g, i, j);
                    cnt++;
                }
            }
        }
        cout << cnt << endl;
        cin >> W >> H;
    }
    
    
    
    return 0;
}
