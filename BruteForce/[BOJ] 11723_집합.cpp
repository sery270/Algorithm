#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
int main() {
    int cnt, x, s = 0;
    char ss[111];
    scanf("%d", &cnt);
    
    
    while(cnt--){
        //cin >> ss;
        scanf("%s", ss);
        if(!strcmp(ss, "add")){
            scanf("%d", &x);
            x -= 1; //0의 자리가 없으므로,
            s = s | (1 << x);
        }else if(!strcmp(ss, "remove")){
            scanf("%d", &x);
            x -= 1; //0의 자리가 없으므로,
            s = s & ~(1 << x);
        }else if(!strcmp(ss,"check")){
            scanf("%d", &x);
            x -= 1; //0의 자리가 없으므로,
            if((s & (1 << x))){
                printf("1\n");
            }else{
                printf("0\n");
            }
        }else if(!strcmp(ss,"toggle")){
            scanf("%d", &x);
            x -= 1; //0의 자리가 없으므로,
            s = s ^ (1 << x);
        }else if(!strcmp(ss, "all")){
            s = 2097151;
        }else if(!strcmp(ss,"empty")){
            s = 0;
        }
        
    }
    
    
    return 0;
}
