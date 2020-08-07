#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int main(){
    int n, k, tmp;
    queue<int> q;
    
    scanf("%d %d", &n, &k);
    
    for(int i = 1; i <= n; i++){
        q.push(i);
    }
    printf("<");
    while(n--){
        for(int i = 1; i< k; i++){
            tmp = q.front();
            q.pop();
            q.push(tmp);
        }
        if(n != 0){
            printf("%d, ", q.front());
            q.pop();
        }else{
            printf("%d", q.front());
            q.pop();
        }
        
    }
    printf(">");
    return 0;
}
