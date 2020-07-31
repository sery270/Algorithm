#include <iostream>
#include <stack>
#include <string>
using namespace std;

int main(){
    string op;
    int N, num;
    stack<int> st;
    cin >> N;
    
    while(N--){
        cin >> op;
        if(op == "push"){
            cin >> num;
            st.push(num);
            continue;
        }else if (op == "pop"){
            cout << (st.empty() ? -1 : st.top()) << endl;
            if(!st.empty()){
                st.pop();
            }
            continue;
        }else if (op == "top"){
            cout << (st.empty() ? -1 : st.top()) << endl;
            continue;
        }else if (op == "size"){
            cout << st.size() << endl;
            continue;
        }else if (op == "empty"){
            cout << (st.empty() ? 1 : 0) << endl;
        }
    }
    return 0;
}
