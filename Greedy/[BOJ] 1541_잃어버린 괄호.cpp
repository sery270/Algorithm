#include <cstdio>
#include <iostream>
using namespace std;
int main() {
    int a, sum =0;
    char c;
    bool nowMinus = false;
    
    scanf("%d",&sum);
    
    while(scanf("%c", &c) && (c == '-' || c == '+')){
        scanf("%d", &a);
        if(c == '+' && nowMinus == true){
            sum -= a;
            //printf("1. %d\n", sum);
            continue;
        }
        if(c == '+' && nowMinus == false){
            sum += a;
            //printf("2. %d\n", sum);
            continue;
        }
        if(c == '-' && nowMinus == true){
            nowMinus = true;
            sum -= a;
            //printf("3. %d\n", sum);
            continue;
        }
        if(c == '-' && nowMinus == false){
            nowMinus = true;
            sum -= a;
            //printf("4. %d\n", sum);
            continue;
        }
    }
    
    printf("%d", sum);
    return 0;
}