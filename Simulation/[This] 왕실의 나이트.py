# 20220115 19:29

move_type = ['HLU','HLD','HRU','HRD','VUL','VUR','VDL','VDR']
dx = [-2,-2,2,2,-1,1,-1,1]
dy = [-1,1,-1,1,-2,-2,2,2]

alpha = ['a','b','c','d','e','f','g','h']

now = input()
y,x = int(alpha.index(now[0])+1), int(now[1])

answer = 0

for i in range(0,8):
  nx, ny = x + dx[i], y+ dy[i]
  if 1<=nx<=8 and 1<=ny<=8 :
    answer += 1

print(answer)

# 20220115 19:42

