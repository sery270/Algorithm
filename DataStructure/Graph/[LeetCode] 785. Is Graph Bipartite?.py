class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        RED = -1
        BLACK = -2
        NONE = 0

        def rotate_color(color):
            if color == RED:
                return BLACK
            else: 
                return RED 

        visited = [False] * len(graph) 
        colored = [NONE] * len(graph)
        color = RED
        for i in range(len(graph)):
            if visited[i]:
                continue
            else:
                q = [i]
                while q:
                    nq = []
                    color = rotate_color(color)
                    for now in q:
                        visited[now] = True
                        if colored[now] == NONE:
                            colored[now] = color
                        else:
                            if colored[now] != color:
                                return False
                        for nh in graph[now]:
                            if visited[nh]:
                                continue
                            else:
                                nq.append(nh)
                    q = nq
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

            - BFS
                0       -1
               / \
              1   3     -2  
             /
            2           -1

            tc5) 

                1 - 2
                 \  |
                    0

            res : False

            - BFS
                    0       -1
                   / \
                  1   2     -2

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
            
    3) cycle -> visisted
            if visisted[node.val]: # already visited
                pass
            else: # visit ! 
                nq.append()
            
    4) graph
        - BFS
            q = []
            while q:
                nq = []
                for now in q:
                    if !visisted[now.val]:
                        nq.append(now)
                        visisted[now] = true
                q = nq

    5) Undirected graph

            
        - BFS
            for i in range(len(graph)):
                if visited[i]:
                    continue
                else:
                    q = [i]
                    while q:
                        nq = []
                        for now in q:
                            visited[now] = True
                            for nh in graph[now];
                                if visited[nh]:
                                    contiue
                                else:
                                    nq.append(nh)
                        q = nq
                        
                        
                        
            tc1)
                1 - 0
                |   
                2   3

            res : True
            
            visited     : TTTT
            i           : 3
            q           : []
            nq          : []
            
                        0       R
                       /    
                      1         B
                     /
                    2           R
                   
                   3
                   
            tc5) 

                1 - 2
                 \  |
                    0
            res : False
            
                    0       B
                   /
                  1         
                 /
                2
                    
  
            visited     : TTT
            i           : 0
            q           : [2]
            now         : 2
            nq          : []
            colored     : BRR
            color       : B
                
        6) colored
            RED = -1
            BLACK = -2
            NONE = 0
            
            colored = [NONE] * len(graph)
            color = RED
            for i in range(len(graph)):
                if visited[i]:
                    continue
                else:
                    q = [i]
                    while q:
                        nq = []
                        color = rotate_color(color)
                        for now in q:
                            visited[now] = True
                            if colored[now] == NONE:
                                colored[now] = color
                            else:
                                if colored[now] != color:
                                    return False
                            for nh in graph[now]:
                                if visited[nh]:
                                    contiue
                                else:
                                    nq.append(nh)
                        q = nq
            
        7) rotate_color
            def rotate_color(color):
                if color == RED:
                    return BLACK
                else: 
                    return RED 
4. Summarize

def isBipartite(self, graph: List[List[int]]) -> bool:
    RED = -1
    BLACK = -2
    NONE = 0
    
    def rotate_color(color):
        if color == RED:
            return BLACK
        else: 
            return RED 

    colored = [NONE] * len(graph)
    color = RED
    for i in range(len(graph)):
        if visited[i]:
            continue
        else:
            q = [i]
            while q:
                nq = []
                color = rotate_color(color)
                for now in q:
                    visited[now] = True
                    if colored[now] == NONE:
                        colored[now] = color
                    else:
                        if colored[now] != color:
                            return False
                    for nh in graph[now]:
                        if visited[nh]:
                            contiue
                        else:
                            nq.append(nh)
                q = nq
    
    
                   
                  
            
            
            
                    
            
            
            
            
                        
                
                        
                    
                        
            
            
            
            
            
            
            
            
            
            
        

'''