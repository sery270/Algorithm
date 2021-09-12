from collections import deque
import sys

MAX = 100000
sys.setrecursionlimit(MAX*2)
N, K = map(int,input().split())
queue = deque([N])
before = [-1 for _ in range(MAX+1)]
path = [K]

while queue :

  now = queue.popleft()
  
  if 0<= now-1 <= MAX:
    if before[now-1] == -1 :
      queue.append(now-1)
      before[now-1] = now
      if now-1 == K :
        break
  if 0<= now+1 <= MAX:
    if before[now+1] == -1 :
      queue.append(now+1)
      before[now+1] = now
      if now+1 == K :
        break
  if 0<= now*2 <= MAX:
    if before[now*2] == -1 :
      queue.append(now*2)
      before[now*2] = now
      if now*2 == K :
        break
  

def find_path(K):
  if before[K] == N :
    path.append(before[K])
    return
  path.append(before[K])
  find_path(before[K])


if N == K :
  print(0)
  print(N)
else: 
  find_path(K)
  path.reverse()  
  print(len(path)-1)
  for p in path:
    print(p, end = " ")

  

