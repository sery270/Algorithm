#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int sol = 99999999, sum = 0;

int main(){
    int N;
    scanf("%d", &N);
    
    // 순열
    vector<int> list(N);
    for(int i=0;i<N; i++){
        list[i] = i+1;
    }
    
    // 비용행렬
    vector<vector<int>> cost(N,vector<int>(N));
    for(int i=0;i<N; i++){
        for(int j=0;j<N; j++){
            scanf("%d", &cost[i][j]);
            // 0일땐, 이동이 불가능한 경로이므로, sol의 고려대상이 아님. 최소값이 될 수 없게 큰 수로 초기화 함
            if(cost[i][j] == 0){
                cost[i][j] = 99999999;
            }
        }
    }
    
    do{
        sum = 0;
        for(int i =0; i<N-1; i++){
            sum += cost[list[i]-1][list[i+1]-1];
        }
        sum += cost[list[N-1]-1][list[0]-1];
        sol = sol < sum ? sol : sum;
        
    } while (next_permutation(list.begin(), list.end()));
    
    printf("%d", sol);
    
    return 0;
}
