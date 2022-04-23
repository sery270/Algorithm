class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        RED = -1
        BLACK = -2
        NONE = 0
        colored = [NONE] * len(graph)
        visited = [False] * len(graph)
        
        
        def rotate_color(color):
            if color == RED:
                return BLACK
            else: 
                return RED 
        
        def dfs(node, color):
            color = rotate_color(color)
            visited[node] = True
            colored[node] = color 
            for nh in graph[node]:
                if visited[nh]:
                    if colored[nh] == color:
                        return False
                    continue
                else:
                    if dfs(nh, color) == False:
                        return False
            return True
            
        for i in range(len(graph)):
            if visited[i]:
                continue
            else:
                if dfs(i, BLACK) == False:
                    return False
        return True
        
'''

1. Problem is..?
    - val == ix 
    - directed ? 

2. TC
    tc1)
            1 - 0
            |   |
            2   3
            
    res : True
    
    tc2) n = 1
            0
    res : False
    
    tc3) n = 2
            1 - 0
    res : True
    
    tc4) 
        1 - 2
            |
            0
    res : True
    
    tc5) 
    
        1 - 2
         \  |
            0
    res : False
    
    tc6) n = 2
            1  0
    res : True
    
    tc7) 
        1  2  0
    res : False
    
3. Brain Storming
    1) draw
            tc1)
                1 - 0
                |   |
                2   3

            res : True

            - DFS
                    0 (-1)
                   /      \
                  1 (-2)   3 (-2)
                 /
                2 (-1)


            tc5) 

                1 - 2
                 \  |
                    0

            res : False
            
            - DFS
                    0 (-1)
                   /
                  1 (-2)
                 /
                2 (-1)

    ================================
    
    2) tree 
        - BFS
        q
        nq

        q = []
        while q: 
            nq = []
            for now in q:
                nq.append(now)
            q = nq
                
        - DFS
        def helper()
            if node:
                if node.left:
                    helper(node.left)
                if node.right:
                    helper(node.right)
                    
    3) cycle -> visisted
            if visisted[node.val]: # already visited
                pass
            else: # visit ! 
                nq.append()
            
    4) graph
        - DFS
        
        visited = [False] * len(graph)
        
        def dfs(node):
            visisted[node] = True
            for nh in graph[node]:
                if visisted[nh]:
                    continue
                else:
                    dfs(nh) 
    

    5) Undirected graph
    
        for i in range(len(graph)):
            if visited[i]:
                continue
            else:
                dfs(i)
    
    6) colored

            tc5) 

                1 - 2
                 \  |
                    0

            res : False
            
            visited : TTT
            colored : RBR
            i       : 0
            color   : R
            
            - DFS
                   (0, B) RF
                   /        
                (1, R) RF
                /
            (2, B)  RF
                
                
                
            tc1)
                1 - 0
                |   |
                2   3

            res : True
            
            visited : TTTT
            colored : BRBR
            i       : 0
            color   : R
            
            - DFS
                    (0, R) RT 
                /           \
            (1, B) RT           (3, B) RT
            /
        (2, R) RT
                    
                 
                 
                 

        colored = [NONE] * len(graph)
        visited = [False] * len(graph)
        
        def dfs(node, color):
            color = roate_color(color)
            visisted[node] = True
            colored[node] = color 
            for nh in graph[node]:
                if visisted[nh]:
                    if colored[nh] == color:
                        return False
                    continue
                else:
                    if dfs(nh, color) == False:
                        return False
            return True
                    
    7) rotate_color
        skip
        
4. Summarize
    def isBipartite(self, graph: List[List[int]]) -> bool:
        RED = -1
        BLACK = -2
        NONE = 0
        colored = [NONE] * len(graph)
        visited = [False] * len(graph)
        
        
        def rotate_color(color):
            if color == RED:
                return BLACK
            else: 
                return RED 
        
        def dfs(node, color):
            color = roate_color(color)
            visisted[node] = True
            colored[node] = color 
            for nh in graph[node]:
                if visisted[nh]:
                    if colored[nh] == color:
                        return False
                    continue
                else:
                    if dfs(nh, color) == False:
                        return False
            return True
            
        for i in range(len(graph)):
            if visited[i]:
                continue
            else:
                if dfs(i, BLACK) == False:
                    return False
        return True
                    
            
            
            
            
                        
                
                        
                    
                        
            
            
            
            
            
            
            
            
            
            
        

'''