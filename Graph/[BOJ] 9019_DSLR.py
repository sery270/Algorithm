from collections import deque
# 상수
# T = map(int,input())
# 변수
T = int(input())
MAX = 10000

def integer(n_str):
  n = 0
  i = 3
  for j in n_str:
    # print(j)
    n += int(j) * (10 ** i)
    i -= 1
  return n

def D(n):
  return 2*n % 10000
def S(n):
  if n == 0:
    n = 9999
  else:
    n -= 1
  return n

def L(n):
  n_str = deque(str(n))
  i = 4-len(n_str)
  # padding 0
  for _ in range(i):
    n_str.appendleft('0')
  
  tmp_str = n_str.popleft()
  n_str.append(tmp_str)
  # print(n_str)
  n_str = list(n_str)


  n_str = integer(n_str)
  return n_str

def R(n):
  n_str = deque([str(n)])
  i = 4-len(n_str)
  # padding 0
  for _ in range(i):
    n_str.appendleft('0')
  tmp_str = n_str.pop()
  n_str.appendleft(tmp_str)
  n_str = list(n_str)
  n_str = integer(n_str)
  return n_str


for _ in range(T):
  A, B = map(int, input().split())
  before = [(-1,'') for _ in range(MAX)]
  path = [B]

  queue = deque([A])

  while queue:
    now = queue.popleft()
    # print('now')
    # print(now)
    if 0<= D(now) < MAX:
      if before[D(now)][0] == -1 :
        queue.append(D(now))
        before[D(now)] = (now, 'D')
        if D(now) == B :
          break
    if 0<= S(now) < MAX:
      if before[S(now)][0] == -1 :
        queue.append(S(now))
        before[S(now)] = (now, 'S')
        if S(now) == B :
          break
    if 0<= L(now) < MAX:
      if before[L(now)][0] == -1 :
        queue.append(L(now))
        before[L(now)] = (now, 'L')
        if L(now) == B :
          break
    if 0<= R(now) < MAX:
      if before[R(now)][0] == -1 :
        queue.append(R(now))
        before[R(now)] = (now, 'R')
        if R(now) == B :
          break

  k = B
  while 1:
    if before[k][0] == A:
      path.append(before[k][1])
      break
    path.append(before[k][1])
    k = before[k][0]
  path.reverse()  
  for p in path:
    print(p, end = '')
