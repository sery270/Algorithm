#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int N, tmp;
int maxSol = -2147483646; // 최대 값
int minSol = 2147483646; // 최대 값
vector<int> list;
// +, -, *, /
vector<int> opList;

// Count, Result, opList
void go(int nowC, int nowR,int p, int m, int mt, int d) {
    if(nowC > N-1){
        return;
    }
    if(nowC == N-1){
        maxSol = maxSol < nowR ? nowR : maxSol;
        minSol = minSol > nowR ? nowR : minSol;
        return;
    }
    if(nowC < N-1){
        if (p>0) go(nowC+1, nowR + list[nowC+1], p-1, m, mt, d);
        if (m>0) go(nowC+1, nowR - list[nowC+1], p, m-1, mt, d);
        if (mt>0) go(nowC+1, nowR * list[nowC+1], p, m, mt-1, d);
        if (d>0) go(nowC+1, int(nowR / list[nowC+1]), p, m, mt, d-1);
    }
    return;
}

int main(){
    scanf("%d", &N);
    for (int i =0; i<N; i++) {
        scanf("%d", &tmp);
        list.push_back(tmp);
    }
    for (int i =0; i<4; i++) {
        scanf("%d", &tmp);
        opList.push_back(tmp);
    }
    go(0, list[0], opList[0], opList[1], opList[2], opList[3]);

    // 아래 처럼 하면 3번이나 더 불필요한 재귀 호출을 하게 됨 
    // if (opList[0]>0) go(1, list[0] + list[1], opList[0]-1, opList[1], opList[2], opList[3]);
    // if (opList[1]>0) go(1, list[0] - list[1], opList[0], opList[1]-1, opList[2], opList[3]);
    // if (opList[2]>0) go(1, list[0] * list[1], opList[0], opList[1], opList[2]-1, opList[3]);
    // if (opList[3]>0) go(1, int(list[0] / list[1]), opList[0], opList[1], opList[2], opList[3]-1);
    
    printf("%d\n%d\n", maxSol, minSol);
    
    return 0;
}
