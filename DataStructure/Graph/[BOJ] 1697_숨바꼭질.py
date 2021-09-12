from collections import deque

MAX = 200000
N, K = map(int, input().split())
q = deque([N])
before = [-1] * (MAX+1)

while q:
  now = q.popleft()

  if 0 <= now-1 <= MAX:
    if before[now-1] == -1 :
      q.append(now-1)
      before[now-1] = now
      if now-1 == K :
        break

  if 0 <= now+1 <= MAX:
    if before[now+1] == -1 :
      q.append(now+1)
      before[now+1] = now
      if now+1 == K :
        break

  if 0 <= now*2 <= MAX:
    if before[now*2] == -1 :
      q.append(now*2)
      before[now*2] = now
      if now*2 == K :
        break

now= K
cnt = 0

while 1 :
  if before[now] == N :
    cnt += 1
    break
  now = before[now]
  cnt += 1

if N == K:
  cnt = 0

print(cnt)