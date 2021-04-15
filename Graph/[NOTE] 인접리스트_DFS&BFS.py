from collections import deque

N, M, V = map(int,input().split())
DFSvisited = [False for _ in range(N+1)]
BFSvisited = [False for _ in range(N+1)]
# print(DFSvisited)
# print(BFSvisited)


# 인접 리스트 입력
graph = [[] for _ in range(N+1)]
for i in range(M):
  node, node2 = map(int,input().split())
  # 무가중치, 무방향
  # 연결됨 & 무가중치 -> 0
  graph[node].append((node2,0))
  graph[node2].append((node,0))
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

