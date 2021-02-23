#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
int k;
vector<int> s;

void go(string now, int i, int cnt){
    if(6 == cnt){
        printf("%s\n", now.c_str());
        return;
    }
    if(cnt > 6 || i >= k) return;
    go(now+to_string(s[i])+" ", i+1, cnt+1);
    go(now, i+1, cnt);
    
}

int main(){
    scanf("%d", &k);
    do{
        s.resize(k);
        for(int i = 0; i<k; i++){
            scanf("%d", &s[i]);
        }
        go("", 0, 0);
        printf("\n");
        scanf("%d", &k);
    }while(k != 0);
    
    return 0;
}
