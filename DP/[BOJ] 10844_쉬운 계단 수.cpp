#include <cstdio>
#include <vector>
using namespace std;
	
vector < vector <long long> > mem(101, vector<long long>(10));
int N;
int sol = 0;


int main(){
    scanf("%d", &N);
    mem[1][0] = 0;
    for(int i =1 ; i<10;i++){
        mem[1][i] = 1;
    }

    //bottom-up
    for(int n =2; n< N; n++){
        for(int end = 0; end<10; end++){
            if(end == 0){
                mem[n][end] = mem[n-1][1];
            }else if(end == 9){
                mem[n][end] = mem[n-1][8];
            }else{
                mem[n][end] = mem[n-1][end-1] + mem[n-1][end+1] ;
            }
        }
    }

    for(int i = 0; i<10; i++){
        sol += mem[N][i];
    }

    printf("%d", sol);
    
    return 0;
}
