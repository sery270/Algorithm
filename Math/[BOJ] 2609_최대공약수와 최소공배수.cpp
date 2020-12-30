#include <iostream>
#include <stdio.h>
#include <vector>


int GCD(int a, int b){
    if(a == 0){
        return a;
    }else{
        return GCD(b, a%b);
    }
}
int LCM(int a, int b){
    int gcd = GCD(a,b);

    return a * b / gcd;
}

int main(){
    int a,b;
    scanf("%d %d", &a, &b);
    printf("%d\n", GCD(a,b));
    printf("%d\n", LCM(a,b));
    return 0;
}