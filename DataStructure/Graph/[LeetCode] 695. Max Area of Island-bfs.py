class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    # marked visited
                    grid[x][y] = 2
                    
                    # BFS setting
                    q = [(x,y)]
                    cnt = 1
                    
                    # starting BFS
                    while q:
                        nq = []
                        for a,b in q:
                            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                                if 0<=a+dx<len(grid) and 0<=b+dy<len(grid[0]) and grid[a+dx][b+dy] == 1:
                                    cnt += 1
                                    nq.append((a+dx,b+dy))
                                    # marked visited
                                    grid[a+dx][b+dy] = 2
                        q = nq 
                    
                    if answer < cnt:
                        answer = cnt
        return answer
                        

        
        
'''
0. test
      2 1 0
      0 1 0
      0 0 0
                    
    answer      : 0
    
    q           : [(0,0)]
    nq          : []
    cnt         : 1
    
    
    
                            (0,0)
                            
    

1. Problem is...?
    a) m,n matrix
    b) maximum area 
    
2. TC
    tc1)
      1 0
      0 1
    res     : 1
    
    
    tc2)
      1
      
    res     : 1
    
    tc3)
      0
    res     : 0
    
    
    tc4)
    
      1 1 0
      0 1 0
      0 0 0
    
    res     : 3    
    
    
3. Brain Storming
    a) draw
    
    U_D_L_R
    
    0<=x<=len(matrix)
    && 
    0<=y<=len(matrix[0])
    && 
    matrix[x][y] == 1
    
      2 2 0
      0 2 0
      0 0 0
    
                    (0,0)
                /         
            (0,1)         
            /
        (1,1)
        
        
            
                    
                    
        
    b) visisted
        mark visited => 2
        
    c) qseudo-tree
        1. bfs)
            q       : []
            nq      : []
            
            
            q = []
            cnt = 0
            nCnt = 0
            
            while q:
                nq = []
                now = q.top()
                for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if ~~:
                        nq.append()
                
                q = nq
            if cnt < nCnt:
                cnt = nCnt
            
            
            
                
            
            
            
        
    0<=x<=len(matrix)
    && 
    0<=y<=len(matrix[0])
    && 
    matrix[x][y] == 1
    
    
    
    d) qseudo-graph
        answer = 0
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 1:
                    q = [(x,y)]
                    cnt = 1
                    while q: 
                        nq = []
                        for a,b in [(-1,0),(1,0),(0,-1),(0,1)]:
                            if 0<=x+a<=len(matrix) and 0<=y+b<=len(matrix[0]) and matrix[x+a][y+y] == 1:
                                cnt = cnt+1
                                nq.append((x+a,y+b))
                        q = nq
                    if answer < cnt:
                        answer = cnt 
                                
    
'''