// #include <cstdio>
// #include <vector>
// using namespace std;

// long long max(long long a,long long b){
//     return a>b?a:b ;
// } 

// vector<vector<long long>> a;
// vector<vector<long long>> mem;

// int main(){
//     int T, N;
//     scanf("%d", &T);

//     while ((T--))
//     {
//         scanf("%d", &N);
//         a.resize(N+1, vector<long long> (3));
//         mem.resize(N+1, vector<long long> (3));
//         for(int i =1 ; i<=N; i++){
//             scanf("%lld", &a[i][1]);
//         }
//         for(int i =1 ; i<=N; i++){
//             scanf("%lld", &a[i][2]);   
//         }
//         for(int i =1; i<=N ; i++){
//             mem[i][0] = max(mem[i-1][0], max(mem[i-1][1], mem[i-1][2]));
//             mem[i][1] = max(mem[i-1][0], mem[i-1][2]) + a[i][1];
//             mem[i][2] = max(mem[i-1][0], mem[i-1][1]) + a[i][2];
//         }
//         long long sol = 0;
//         for(int i = 1; i<=N; i++){
//             sol = max(max(sol,mem[i][0]), max(mem[i][1], mem[i][2]));
//         }

//         printf("%lld\n",sol);        
//     }
    

//     return 0;
// }


#include <iostream>

using namespace std;

int n, m, t;
int arr[2][100005];
int dp1[2][100005];

int main() {
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);

    cin >> t;
    while (t--) {
        cin >> n;
        for (int j = 0; j < 2; j++) {
            for (int i = 1; i <= n; i++) {
                cin >> arr[j][i];
                dp1[j][i] = 0;
            }
        }

        dp1[0][1] = arr[0][1];
        dp1[1][1] = arr[1][1];
        for (int i = 2; i <= n; i++) {
            dp1[0][i] = max(dp1[1][i - 1], max(dp1[1][i - 2], dp1[0][i - 2]) ) + arr[0][i];
            dp1[1][i] = max(dp1[0][i - 1], max(dp1[1][i - 2], dp1[0][i - 2]) ) + arr[1][i];
        }
        cout << max(dp1[0][n], dp1[1][n]) << '\n';
    }

    return 0;
}
