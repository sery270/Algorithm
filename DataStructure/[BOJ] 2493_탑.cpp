#include <cstdio>
#include <stack>
#include <utility>
using namespace std;
int n, k;
stack<pair<int, int> > st;
int main() {
    scanf("%d", &n);
    for (int i = 1; i<=n; i++) {
        scanf("%d", &k);
        while (!st.empty()) {
            //스택의 top이 현재 입력값보다 크다면 신호 수신 가능이므로 
            if (st.top().second > k){
                //top의 위치를 출력하고 반복문을 탈출한다. 
                printf("%d ", st.top().first);
                break;
            }
            st.pop();
        }
        //스택이 비었으면 0을 출력한다. 
        if(st.empty()) printf("0 ");
        //그리고 현재 탑을 스택에 push 
        st.push(make_pair(i, k));
    }
}