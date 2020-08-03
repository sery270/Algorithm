#include <iostream>
#include <cstdio>
#include <stack>
using namespace std;

int main(){
    char prev, now;
    int cnt =0;
    stack<char> st;
    
    scanf("%c", &prev);
    scanf("%c", &now);
    st.push(prev);
    
    while(now == '(' || now == ')'){
        if(now == '('){
            if(prev == '('){
                st.push(now);
            }else{
                st.push(now);
            }
        }else{
           if(prev == '('){
                st.pop();
                cnt += st.size();
            }else{
                st.pop();
                cnt++;
            }
            
        }
        prev = now;
        scanf("%c", &now);
        //printf("%d\n", cnt);
    }
    
    printf("%d", cnt);
    return 0;
}
