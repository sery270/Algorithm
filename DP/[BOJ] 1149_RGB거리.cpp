#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> mem(1001, vector<int>(3));
vector<vector<int>> a(1001, vector<int>(3));
int N;

int RGBmin(int a, int b){
	return a<b?a:b ;
}

int main(){\
	cin >> N;
	for(int i =1; i<=N; i++){
		cin >> a[i][0]>> a[i][1]>> a[i][2];
	}
	
	mem[1][0] = a[1][0];
	mem[1][1] = a[1][1];
	mem[1][2] = a[1][2];
	
	for(int i =1; i<= N; i++){
		mem[i][0] = RGBmin(mem[i-1][1],mem[i-1][2]) + a[i][0];
		mem[i][1] = RGBmin(mem[i-1][0],mem[i-1][2]) + a[i][1];
		mem[i][2] = RGBmin(mem[i-1][0],mem[i-1][1]) + a[i][2];
			
		
	}
	
	cout << RGBmin(mem[N][0],RGBmin(mem[N][1],mem[N][2])) << endl;
	
	return 0;
}
