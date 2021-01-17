#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;


int main(){
    int e,s,m;
    scanf("%d %d %d", &e, &s,&m);
    
    for(int i = 0;; i++){
        if(i%15 == e-1 && i%28 == s-1 && i%19 == m-1){
            printf("%d", i+1);
            break;
        }
    }
    
    
    return 0;
}
