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
    
    if(prev_permutation(list.begin(), list.end())){
        for(int i =0; i<N; i++){
            printf("%d ", list[i]);
        }
    }else{
        printf("-1");
    }

    return 0;
    
}
