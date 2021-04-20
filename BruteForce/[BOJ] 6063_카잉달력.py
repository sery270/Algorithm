from math import gcd
# 상수
# T = map(int,input())
# 변수
T = int(input())

def lcm(a,b):
  return a*b//gcd(a,b)

while T:
  M, N, x, y = map(int, input().split())

  l = lcm(N,M)

  now_year = -1
  now_x = 1
  now_y = 1

  for i in range(1, l):
    if now_x == x and now_y == y:
      now_year =  i
    # print(now_x, now_y, now_year)
    if now_x < M:
      now_x += 1
    else:
      now_x = 1

    if now_y < N:
      now_y += 1
    else:
      now_y = 1

  # if now_year != -1:
  #   print(now_year+2)
  # else:
  #   print(now_year)

  print(now_year)
  T -= 1