#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> mem(301, vector<int>(3));
vector<int> a(301);
int N;

int sumMAX(int a, int b){
	return a>b?a:b;
}

int main(){
	cin >> N;
	for(int i =1;i <=N; i++){
		cin >> a[i];
	}
	mem[1][0] = 0;
	mem[1][1] = a[1];
	mem[1][2] = a[1];
	for(int i =2; i<=N; i++){
		mem[i][0] = sumMAX(mem[i-1][1], mem[i-1][2]);
		mem[i][1] = mem[i-1][0] + a[i];
		mem[i][2] = mem[i-1][1] + a[i];
	}
	
	cout << sumMAX(mem[N][1], mem[N][2]) << endl;;
	
	return 0;
}
