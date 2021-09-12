#include <stdio.h>
#include <iostream>
#include <vector>
#include <utility>

using namespace std;

//a. 무방향&무가중치
vector<vector<int> > aG;
//한 인덱스는 하나의 정점을 의미

bool DFSvisit[100001] = { false, };

int parent[100001] = { 0, };

int v; //노드의 개수 

void input() {
	cin >> v;
	aG.resize(v + 2);
	int a, b; //간선 정보 
	for (int i = 1; i < v ; i++) {
		cin >> a >> b;
		aG[a].push_back(b);
		aG[b].push_back(a);
	}
}

void DFS(int node) {

		DFSvisit[node] = true;

		for (int i = 0; i<aG[node].size(); i++) {
			int next = aG[node][i];

			if (!DFSvisit[next]) {
				parent[next] = node;
				DFS(next);
			}
		}

	}

void sol() {
		for (int i = 2; i < v + 1; i++) {
			cout << parent[i] << "\n";
		}

}


	int main() {
		input();
		DFS(1);
		sol();


		return 0;
	}
