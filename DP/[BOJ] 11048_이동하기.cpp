#include <cstdio>
#include <vector>
using namespace std;

int N, M, tmp;
vector<vector<int>> list(1001, vector<int>(1001));
//vector<vector<int>> D(1001, vector<int>(1001));

bool ispos(int n, int m){
    return n>0 && n<N+1 && m>0 && m<M+1;
}

int ismax(int a, int b){
    return a>b?a:b;
}


//int dp(int n, int m){
//    if(!ispos(n, m)){
//        return 0;
//    }
//    if(D[n][m] > 0) {
//        return D[n][m];
//    }
//
//    //    D[n][m] = ismax(ismax(D[n-1][m], D[n][m-1]), D[n-1][m-1]) + list[n][m];
//    //    D[n][m] = ismax(ismax(dp(n-1, m-1), dp(n, m-1)), dp(n-1, m)) + list[n][m];
//
//    //    D[n+1][m] = D[n+1][m]<(D[n][m] + list[n+1][m]) ? D[n][m] + list[n+1][m]:D[n+1][m];
//    //    D[n+1][m+1] = D[n+1][m+1]<(D[n][m] + list[n+1][m]) ? D[n][m] + list[n+1][m]:D[n+1][m+1];
//    //    D[n][m+1] = D[n][m+1]<(D[n][m] + list[n+1][m]) ? D[n][m] + list[n+1][m]:D[n][m+1];
//
//
//
//    return D[n][m];
//}


int main(){
    scanf("%d %d", &N, &M);
    for(int i = 1; i<=N; i++){
        for(int j = 1; j<=M; j++){
            scanf("%d", &list[i][j]);
        }
    }
    
    
//    dp(N, M);
    
    for(int n = 1; n<=N; n++){
        for(int m = 1; m<=M; m++){
//            D[n][m] = ismax(ismax(D[n-1][m], D[n][m-1]), D[n-1][m-1]) + list[n][m];
            list[n][m] += ismax(ismax(list[n-1][m], list[n][m-1]), list[n-1][m-1]);
        }
    }
    
    
    
    
//    printf("%d", D[N][M]);
    printf("%d", list[N][M]);
    
    
    return 0;
}

