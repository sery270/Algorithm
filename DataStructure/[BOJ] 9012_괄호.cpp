#include <iostream>
#include <cstdio>
#include <stack>
#include <string>
using namespace std;

char w;
string s;
int i = 0;

string isitVPS(string s){
    stack<char> st;
    for(int i =0; i < s.size(); i++){
        w = s[i];
        if(w == '('){
                st.push(w);
                continue;
            }else{
                if(st.empty()){
                    return "NO";
                }else{
                    if(st.top() == '('){
                        st.pop();
                        continue;
                    }else if (st.top() == ')'){
                        return "NO";
                    }
                }
            }
    }
    
    
    
    if(st.empty()){
        return "YES";
    }else{
        return "NO";
    }
    
    
    
    
}

int main(){
    int n;
    cin >> n;
    while(n--){
        cin >> s;
        cout << isitVPS(s) << endl;
    }

    
    return 0;
}
