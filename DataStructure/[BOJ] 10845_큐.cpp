#include <iostream>
#include <queue>
#include <string>
using namespace std;

int main(){
    int n, m;
    string s;
    cin >> n;
    
    queue<int> q;
    
    while(n--){
        cin >> s;
        
        if(s == "push"){
            cin >> m;
            q.push(m);
            
        }else if(s == "pop"){
            if(q.empty()){
                cout << -1 << endl;
            }else{
                cout << q.front() << endl;
                q.pop();
            }
        }else if (s == "size"){
            cout << q.size() << endl;
        }else if(s == "empty"){
            if(q.empty()){
                cout << 1 << endl;
            }else{
                cout << 0 << endl;
            }
        }else if(s == "front"){
            if(q.empty()){
                cout << -1 << endl;
            }else{
                cout << q.front() << endl;
            }
        }else if(s == "back"){
            if(q.empty()){
                cout << -1 << endl;
            }else{
                cout << q.back() << endl;
            }
        }
        
        
    }
    return 0;
}
