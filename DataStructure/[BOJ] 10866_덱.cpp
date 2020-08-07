#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main(){
    int n,x;
    string s;
    deque<int> dq;
    cin >> n;
    
    
    while(n--){
        cin >> s;
        if(s == "push_back"){
            cin >> x;
            dq.push_back(x);
            
        }else if(s == "push_front"){
            cin >> x;
            dq.push_front(x);

        }else if(s == "pop_front"){
            if(dq.empty()){
                cout << -1 << endl;
            }else{
                cout << dq.front() << endl;
                dq.pop_front();
            }
        }else if(s == "pop_back"){
            if(dq.empty()){
                cout << -1 << endl;
            }else{
                cout << dq.back() << endl;
                dq.pop_back();
            }
        }else if(s == "size"){
            cout << dq.size() << endl;
            
        }else if(s == "empty"){
            if(dq.empty()){
                cout << 1 << endl;
            }else{
                cout << 0 << endl;
            }
            
        }else if(s == "front"){
            if(dq.empty()){
                cout << -1 << endl;
            }else{
                cout << dq.front() << endl;
            }
        }else if(s == "back"){
            if(dq.empty()){
                cout << -1 << endl;
            }else{
                cout << dq.back() << endl;
            }
        }
    }
    
    
    return 0;
}
