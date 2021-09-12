from collections import deque

MAX = 100
N, M = map(int, input().split())
map = [list(map(int, list(input()))) for _ in range(N)]

# 직전 좌표를 튜플로 저장해두는 배열
before = [[0 for _ in range(M) ]for _ in range(N)] 
# before[0][0] =(1,2)
# print(before)

# 좌표 이동을 위한 배열 : 상하좌우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 매개변수의 좌표가 가능한 좌표인지 확인하는 함수 
def possible(x,y):
  return 0<=x and 0<=y and x<M and y<N

# (x,y)
q = deque([])
q.append((0,0))
# print(q)
# i = q.popleft()
# print(i)


while q:
  now = q.popleft()
  now_x = now[0]
  now_y = now[1]
  # print(now)
  for i in range(0,4):
    ix = dx[i]
    iy = dy[i]
    if possible(now_x+ix, now_y+iy):
      if map[now_y+iy][now_x+ix] == 1 and before[now_y+iy][now_x+ix] == 0:
        q.append((now_x+ix,now_y+iy))
        before[now_y+iy][now_x+ix] = (now_x,now_y)
        # cnt += 1 

now = before[N-1][M-1] 
cnt = 0
# print(before)

while 1:
  now_x = now[0]
  now_y = now[1]
  if before[now_y][now_x] == (0,0):
    cnt += 1
    break
  
  cnt += 1
  now = before[now_y][now_x]
  # print(now)
  

print(cnt+2)




