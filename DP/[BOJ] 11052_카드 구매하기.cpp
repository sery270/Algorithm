#include <cstdio>
#include <vector>
using namespace std;

vector<int> P(1001);
vector<int> M(1001);
int N, p, tmpMax;
int main(){
    scanf("%d", &N);
    for(int i = 1; i<=N; i++){
        scanf("%d", &P[i]);
    }

    M[1] = P[1];
    //bottom-up
    for(int i =2; i <= N; i++){
        tmpMax = 0;
        for(int j = 1; i > j ; j++){
            if(M[i] > 0 && M[j] + P[i-j] > tmpMax){
                tmpMax = M[j] + P[i-j];
            }
        }
        if(P[i] > tmpMax){
            tmpMax = P[i];
        }
        M[i] = tmpMax;
    }

    printf("%d", M[N]);
    return 0;
}