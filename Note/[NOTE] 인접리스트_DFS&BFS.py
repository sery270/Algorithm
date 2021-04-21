from collections import deque

N, M, V = map(int,input().split())
DFSvisited = [False for _ in range(N+1)]
BFSvisited = [False for _ in range(N+1)]
# print(DFSvisited)
# print(BFSvisited)


# 인접 리스트 입력
# 세 개의 인덱스, 노드 번호/ 의미 없음 그냥 순서/ 0은 노드 번호, 1은 노드간 비용
# 두 개의 인덱스에 있는 값 (튜플), (노드 번호, 노드 간의 거리)
# 세 개의 인덱스에 있는 값 (정수), 튜플[0] 노드 번호/ 튜플[1] 노드간 비용
# graph[1][2][0] : 1번 node 리스트에 세번째로 저장된 node의 번호 
# graph[1][2][1] : 1번 node와 graph[1][2][0]의 거리/ node1 리스트에 세번째로 저장된 node와의 거리 
graph = [[] for _ in range(N+1)]
for i in range(M):
  node, node2 = map(int,input().split())
  # 무비용, 무방향
  # 연결됨 & 무비용 -> 0
  graph[node].append((node2,0))
  graph[node2].append((node,0))
# 노드 번호 상관 없이 append 되므로, 
# 문제에 "여러 노드 중 작은 것 부터 탐색" 같은 조건이 있으면, 정렬해줘야함
# 노드 번호 순으로 정렬
for i in range(1, N+1):
  graph[i] = sorted(graph[i], key = lambda x: x[0])
# print(graph)


# DFS 인접 리스트
def DFS(g, v):
  DFSvisited[v] = True
  print(v, end=' ')
  for i in g[v]:
    if not DFSvisited[i[0]]:
      DFS(g, i[0])

# BFS 인접 리스트
def BFS(g, v):
  queue = deque([v])
  BFSvisited[v] = True
  while queue:
    now = queue.popleft()
    print(now, end=' ')
    for i in g[now]:
      if not BFSvisited[i[0]]: 
          queue.append(i[0])
          BFSvisited[i[0]] = True






DFS(graph, V)
print()
BFS(graph, V)

