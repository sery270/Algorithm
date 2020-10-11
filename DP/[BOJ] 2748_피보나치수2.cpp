#include <cstdio>
#include <vector>

using namespace std;
int N;
vector<long long> list(91);
int main(){
    scanf("%d", &N);
    list[0] = 0;
    list[1] = 1;
    list[2] = 1;
    for(int i = 3; i<=N; i++){
        list[i] = list[i-1] + list[i-2];
    }
    
    printf("%lld", list[N]);
    
    return 0;
}
