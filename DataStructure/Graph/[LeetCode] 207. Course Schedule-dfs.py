class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        # cycle 기록 범위 : 현재 노드의 탐색 시작과 끝 
        # 현재 노트 탐색 끝나면 -> remove !!
        traced = set()
        # visited 기록 범위 : 탐색 시작과 끝
        visited = [False] * numCourses
        
        def dfs(i):
            # has cycle
            if i in traced:
                return False
            # already visited 
            if visited[i]:
                return True
            
            traced.add(i)
            
            # has cycle ? 
            for y in graph[i]:
                if not dfs(y):
                    return False            
            traced.remove(i)
            visited[i] = True
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True   
'''
- bipartite 가 자연스럽게 풀려야 207 해결
- Topological Sort ( BFS + @ )
    a. condition
        - no cycle
        - directed graph
    b. algorithms
        - 집입차수가 0인 노드
        - 

1. Problem is
    - 0...numCourses-1
    - has cycle -> False
    - undirected graph
    - unconnected graph
    
2. TC
    tc1)
        2
        [[1,0]]
        -----------
        True
    tc2)
        1
        []
        ---------
        True
    tc3)
        2
        [[1,0],[0,1]]
        -----------
        False
    
    tc4)
        3
        [[0,1],[0,2],[1,2]]
        ------------
        True
    
    
3. Brain Storming
    a) draw
    
    b) tree
        - DFS
        def helper()
            if node:
                if node.left:
                    helper(node.left)
                if node.right:
                    helper(node.right)
                    
    c) visisted 
            if visisted[node.val]: # already visited
                pass
            else: # visit ! 
                nq.append()
    
    d) graph
        - DFS
        
        visited = [False] * len(graph)
        
        def dfs(node):
            if visited[node]:
                # visited! ! 
                
            visisted[node] = True
            for nh in graph[node]:
                if not dfs(nh):
                    return False
            
    
    e) has cycle
        # cycle 기록 범위 : 현재 노드의 탐색 시작과 끝 
        # 현재 노트 탐색 끝나면 -> remove !!
        traced = set()
        
        def dfs(i):
            # has cycle
            if i in traced:
                return False
                
            # already visited 
            if visited[i]:
                return True
            
            # 현재 노드 탐색 시작 ! 
            traced.add(i)
            
            # has cycle ? 
            for y in graph[i]:
                if not dfs(y):
                    return False   
                 
            # 현재 노드 탐색 끝 ! 
            traced.remove(i)
            visited[i] = True
            return True
'''