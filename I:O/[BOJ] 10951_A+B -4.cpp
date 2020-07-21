#include <stdio.h>
using namespace std;

int main(){
    int a,b;
    while(scanf("%d %d", &a, &b) != EOF){
        //EOF는 scanf의 에러에 대한 리턴 값이다.
        printf("%d\n", a+b);
    }
    return 0;
}