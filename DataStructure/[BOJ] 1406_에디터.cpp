#include <iostream>
#include <cstdio>
#include <stack>
using namespace std;

char op, str, tmp;
string s;
int m;
stack<char> leftST, rightST;

void input(){
    cin >> s;
    for(int i =0; i< s.length(); i++){
        leftST.push(s[i]);
        
    }
    scanf("%d", &m);
}

int main(){
    input();
    for(int i =0; i< m; i++){
        //scanf("%c", &op);
        cin >> op;
        //cout << op << endl;
        if( op == 'L'){
            if(!leftST.empty()){
                tmp = leftST.top();
                leftST.pop();
                rightST.push(tmp);
            }
            
        }else if( op == 'D'){
            if(!rightST.empty()){
                tmp = rightST.top();
                rightST.pop();
                leftST.push(tmp);
            }
        }else if(op == 'B'){
            if(!leftST.empty()){
                leftST.pop();
            }
        }else if(op == 'P'){
            //scanf("%c", &str);
            cin >> str;
            //cout << "dsasdf" << endl;
            leftST.push(str);
        }
    }
    
    int leftSTSize = (int)leftST.size();
    while(leftSTSize--){
        tmp = leftST.top();
        leftST.pop();
        rightST.push(tmp);
    }
    
    int rightSTSize = (int)rightST.size();
    while(rightSTSize--){
        cout << rightST.top();
        rightST.pop();
    }
    
    return 0;
}
