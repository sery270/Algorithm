import sys

MAX = 100000
sys.setrecursionlimit(MAX)

def solution(v):
    global dx, dy, visited, area,area_list
    # 좌표 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    # 방문 기록 
    visited = []
    # 영역 넓이, 넓이 리스트 
    area, area_list = 0, []
    # 맵의 크기 
    global r
    r = 0 
    global c
    c = 0

    answer = 1
    # global r,c
    c,r = len(v), len(v[0])

    if c == 1 and r == 1 and v[0][0] == 0:
      answer = [0,0]
    else: 
    
      visited = [[False]*r for _ in range(c)]

      for i in range(c):
          for j in range(r):
              if v[i][j] == 1 and visited[i][j] == False:
                    area = 0
                    dfs(i,j,v,r,c)
                    area_list.append(area)

      print(area_list)
      area_list.sort(reverse=True)
      answer = [len(area_list),area_list[0]]
    return answer

def dfs(x, y,v,r,c):
    global dx, dy, visited, area, area_list
    
    area = area + 1
    visited[x][y] = True
    
    for i in range(4):
          nx, ny = x + dx[i], y + dy[i]
          # print(nx,ny)
          if 0 <= nx < c and 0 <= ny < r:
                # print(area)
                if v[nx][ny] == 1 and visited[nx][ny] == False:
                    dfs(nx, ny, v,r,c)

print(solution([[0]]))