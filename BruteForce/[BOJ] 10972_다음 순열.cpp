// #include <iostream>
// #include <vector>
// using namespace std;

// int N, tmp;
// vector <int> v;

// void input(){
//     cin >> N;
//     v.resize(N);
//     for(int i =0; i<N; i++){
//         cin >> tmp;
//         v[i] = tmp;
//     }
    
// }

// bool next_p(vector<int> &a, int n){
//     int i , j;
    
//     i = N-1;
//     while(i > 0 && v[i-1] >= v[i]){
//         i -= 1;
//     }
//     if(i <=0){
//         return false;
//     }
    
//     j = N-1;
//     while(v[j] <= v[i-1]){
//         j -= 1;
//     }
//     swap(v[i-1], v[j]);
//     j = N-1;
    
//     while(i < j){
//         swap(v[i], v[j]);
//         i += 1;
//         j -= 1;
//     }
    
//     return true;
    
// }


// int main(){
//     input();
    
//     if(next_p(v, N)){
//         for(int i = 0; i<N; i++){
//             cout << v[i] << ' ';
//         }
//     }else{
//         cout << "-1";
//     }
    
    
    
//     return 0;
// }
#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main(){
    int N;
    scanf("%d", &N);
    vector<int> list(N);
    for(int i = 0; i<N; i++){
        scanf("%d", &list[i]);
    }
    
    if(next_permutation(list.begin(), list.end())){
        for(int i =0; i<N; i++){
            printf("%d ", list[i]);
        }
    }else{
        printf("-1");
    }

    return 0;
    
}
