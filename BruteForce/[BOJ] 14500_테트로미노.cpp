#include <stdio.h>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

// 맵
vector<vector<int>> map;
int N, M;

// 테트로미노 좌표 표현
vector<vector<int>> posN(19, vector<int>(3));
vector<vector<int>> posM(19, vector<int>(3));


int sol = 0;



bool isPossible(int n, int m, int pos){
    
    bool r = true;
    
    for(int i =0; i<3; i++){
        if(n+posN[pos][i]<N && 0<=n+posN[pos][i] && m+posM[pos][i] < M && 0<= m+posM[pos][i]){
        
        } else{
            r = false;
        }
            
    }
    

    return r;
}

int posSum(int n, int m, int pos){
    
    int posSum = 0;
    
    for(int i =0; i<3; i++){
        posSum += map[n+posN[pos][i]][m+posM[pos][i]];
    }
    
    posSum += map[n][m];
    
    return posSum;
}

int main(){
    
    // ㅁㅁㅁㅁ
    posN[0] = {0,0,0};posN[1] = {1,2,3};
    // ㅁㅁ
    // ㅁㅁ
    posN[2] = {0,1,1};
    // ㅁ
    // ㅁ
    // ㅁㅁ
    posN[3] = {1,2,2};posN[4] = {0,-1,-2};posN[5] = {0,1,2};posN[6] = {0,1,2};posN[7] = {1,1,1};posN[8] = {0,0,-1};posN[9] = {0,0,1};posN[10] = {0,0,1};
    // ㅁ
    // ㅁㅁ
    //  ㅁ
    posN[11] = {1,1,2};posN[12] = {0,-1,1};posN[13] = {0,-1,-1};posN[14] = {0,1,1};
    // ㅁㅁㅁ
    //  ㅁ
    posN[15] = {0,0,1};posN[16] = {0,0,-1};posN[17] = {1,1,2};posN[18] = {0,-1,1};
    
    
    posM[0] = {1,2,3};posM[1] = {0,0,0};
    posM[2] = {1,0,1};
    posM[3] = {0,0,1};posM[4] = {1,1,1};posM[5] = {1,0,0};posM[6] = {1,1,1};posM[7] = {0,1,2};posM[8] = {1,2,2};posM[9] = {1,2,0};posM[10] = {1,2,2};
    posM[11] = {0,1,1};posM[12] = {1,1,0};posM[13] = {1,1,2};posM[14] = {1,1,2};
    posM[15] = {1,2,1};posM[16] = {1,2,1};posM[17] = {0,1,0};posM[18] = {1,1,1};
    
    
    
    scanf("%d %d", &N, &M);
    
    
    
    int tmpNum;
    for(int i =0; i<N; i++){
        vector<int> tmp;
        for(int j=0; j<M; j++){
            scanf("%d",&tmpNum);
            tmp.push_back(tmpNum);
        }
        map.push_back(tmp);
    }
    
    
    for(int pos = 0; pos<19; pos++){
        for(int i =0; i<N; i++){
            for(int j=0; j<M; j++){
                if(isPossible(i,j,pos)){
                    int tmp = posSum(i, j, pos);
                    sol = sol < tmp ? tmp : sol;
                }
    
            }
    
        }
    }
    
    printf("%d", sol);
    

    
    return 0;
}
