#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace  std;

int L,C;
vector<char> list;

bool check(string &pw){
    int ja = 0;
    int mo = 0;

    for(char c : pw){
        if( c == 'a'|| c == 'e'|| c == 'i'|| c == 'o'|| c == 'u' ){
            mo++;
        }else{
            ja++;
        }
    }

    return ja>=2 && mo>=1;
}

void go(string pw, int i){

    if(L == pw.length()){
        if(check(pw)){
            printf("%s\n", pw.c_str());
        }
        return;
    }
    if(i >= C){
        return;
    }
    go(pw+list[i], i+1);
    go(pw, i+1);
}


int main(){
    scanf("%d %d", &L, &C);
    list.resize(C);
    for(int i = 0; i<C; i++){
        scanf("%s", &list[i]);
    }

    sort(list.begin(), list.end());
    go("", 0);

    return 0;
}
