from collections import deque

N, M, V = map(int,input().split())
DFSvisited = [False for _ in range(N+1)]
BFSvisited = [False for _ in range(N+1)]
# print(DFSvisited)
# print(BFSvisited)

# 인접 행렬 입력
# 두 개의 인덱스, 기준 노드 번호/ 연결된 노드 번호 
# 두 개의 인덱스에 있는 값 (정수), 노드 간의 거리
INF = 999999999 # 연결 안된 경우
graph2 =[[INF]*(N+1) for _ in range(N+1)]
for i in range(M):
  node, node2 = map(int,input().split())
  # 무비용, 무방향
  # 연결됨 & 무비용 -> 0
  # 연결안됨 -> INF
  graph2[node][node2] = 0
  graph2[node2][node] = 0

# 각 노드의 자리가 인덱스로 정해져 있으므로, 
# 노드 번호 순으로 정렬 안해도 됨 
print(graph2)

# DFS 인접 행렬 
def DFS(g, v):
  DFSvisited[v] = True
  print(v, end=' ')
  for i in range(1, N+1):
    # INF (의미 없는 값)으로 채워졌을 수도 있으니 확인  
    if g[v][i] != INF and not DFSvisited[i]:
      DFS(g, i)
  

# BFS 인접 행렬 
def BFS(g, v):
  queue = deque([v])
  BFSvisited[v] = True
  while queue:
    now = queue.popleft()
    print(now, end=' ')
    for i in range(1, N+1):
        # INF (의미 없는 값)으로 채워졌을 수도 있으니 확인  
      if g[now][i] != INF and not BFSvisited[i]: 
          queue.append(i)
          BFSvisited[i] = True



DFS(graph, V)
print()
BFS(graph, V)
