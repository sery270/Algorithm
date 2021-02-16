#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int sol = 0, sum = 0;;

int main(){
    int N;
    scanf("%d", &N);
    vector<int> list(N);
    for(int i=0;i<N; i++){
        scanf("%d", &list[i]);
    }
    
    sort(list.begin(), list.end());

    do{
        sum = 0;
        for(int i =0; i<N-1; i++){
            int tmp = list[i] - list[i+1];
            sum += tmp > 0 ? tmp: -tmp;
        }
        
        sol = sol < sum ? sum : sol;
    
    } while (next_permutation(list.begin(), list.end()));
    
    printf("%d", sol);
    
    return 0;
}
