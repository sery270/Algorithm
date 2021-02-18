#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int T;
int tmp;

int go(int sum, int goal) {
    if(sum > goal){
        return 0;
    }
    if(sum == goal){
        return 1;
    }
    int nowCnt =0;
    for(int i =1; i<4;i++){
        nowCnt += go(sum+i, tmp);
    }
    return nowCnt;
}

int main(){
    scanf("%d", &T);
    for (int i =0; i<T; i++) {
        scanf("%d", &tmp);
        printf("%d\n", go(0, tmp));
    }
    
    
    
    return 0;
}
