// #include <stdio.h>
// using namespace std;

// int main(){
//     int T, a, b;
//     scanf("%d", &T);
    
//     for(int i =0; i<T; i++){
//         scanf("%d,%d", &a, &b);
//         printf("%d\n", a+ b);
//     }
    
    
//     return 0; 
// }

#include <stdio.h>
using namespace std;

int main(){
    int T,a,b;
    scanf("%d", &T);
    for(int i = 1; i <=T; i++){
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d", i, a+b);
    }
    
    return 0;
}