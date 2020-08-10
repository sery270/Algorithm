#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;
 

int main(){
    char c;
    int ix;
    vector<int> clist(30);
    while(1){
        scanf("%c", &c);
        ix = (int)c;
        if(c >= 97 && c < 123){
            clist[ix-97]++;
        }else break;
        
    }
    
    for(int i =0 ; i< 26; i++){
        printf("%d ", clist[i]);
    }
    return 0;
}


//백준 코드인데 왕 간결해서 가져옴

// #include <algorithm>
// #include <iostream>
// #include <string>
// using namespace std;
// int main() {
//     string s;
//     cin >> s;

//     for (int i='a'; i<='z'; i++) {
//         cout << count(s.begin(), s.end(), i) << ' ';
//     }

//     cout << '\n';
    

//     return 0;
// }