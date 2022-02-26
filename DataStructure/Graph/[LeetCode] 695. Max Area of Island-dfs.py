class Solution:
    def dfs(self, grid,i,j):
        if 0<=i<len(grid) and 0<=j<len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = 2
            cnt = 1
            for a,b in [(-1,0), (1,0), (0,-1), (0,1)]:
                cnt += self.dfs(grid, i+a, j+b)
            return cnt
        else:
            return 0
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        res = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 1:
                    now = self.dfs(grid,i,j)
                    if res < now:
                        res = now
        return res
            
                    
                    
        
        
'''
        def helper(grid, i, j):
            if 0<= i < len(grid) and 0<= j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 2
                cnt = 1
                for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       cnt += self.helper(matrix, i+a, j+b)
                return cnt
            else:
                return 0
1. Problem is ?
    a) max area 
    b) grid is not nullable
    c) 4-directionally
    
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
    
    
    tc5)
      1 1 0
      0 0 1
      0 1 1
      
    res     : 3
    
3. Brain Storming
    1) draw
      tc4)
    
      1 1 0
      0 1 0
      0 0 0
      
      move : U - D - L - R
                                    (0,0)
                                                 \
                            (-1,0) (1,0) (0,-1) (0,1)
                                                    \
                                            (-1,1) (1,1) (0,0) (0,2)
                                                    /
                                            (0,1) (2,1) (1,0) (1,2)
                                            
      
      
      
      
      cnt : 1, 1, 1
                                    
      
      
      
    2) visited
        mark as 2
        
    3) pseudo - tree
        
    4) pseudo - graph
        def helper(grid, i, j):
            if 0<= i < len(grid) and 0<= j < len(grid[i]) and grid[i][j] == 1:
                grid[i][j] = 2
                cnt = 1
                for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                       cnt += self.helper(matrix, i+a, j+b)
                return cnt
            else:
                return 0
4. Summarize
    

'''