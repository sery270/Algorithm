class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 진입차수 
        indegree = [0] * numCourses
        # 그래프 
        graph = collections.defaultdict(list)
        
        # 그래프, 진입차수 init
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1 # 진입차수 
        q = []
        
        for i in range(0, numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            nq = []
            for now in q:
                for i in graph[now]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        nq.append(i)
            q = nq
        for i in range(0, numCourses):
            if indegree[i] != 0:
                return False
        return True
        
'''
- bipartite 가 자연스럽게 풀려야 207 해결
- Topological Sort ( BFS + @ )
    a. condition
        - no cycle
        - directed graph
    b. algorithms
        - 집입차수가 0인 노드 삽입
        - BFS + 간선삭제 

1. Problem is
    - 0...numCourses-1
    - has cycle -> False
    - directed graph
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
        - BFS
        q
        nq

        q = []
        while q: 
            nq = []
            for now in q:
                nq.append(now)
            q = nq
                    
    c) visisted 
            if visisted[node.val]: # already visited
                pass
            else: # visit ! 
                nq.append()
    
    d) graph
        - BFS
            q = []
            while q:
                nq = []
                for now in q:
                    if !visisted[now.val]:
                        nq.append(now)
                        visisted[now] = true
                q = nq

    
    5) make graph for topological_sort
        # 진입차수 
        indegree = [0] * (v + 1)
        # 그래프 
        graph = collections.defaultdict(list)
        
        # 그래프, 진입차수 init
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1 # 진입차수 
            
    6) topological Sort ( BFS + @ )
        
        q = []
        
        for i in range(0, numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            nq = []
            for now in q:
                for i in graph[now]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        nq.append(i)
            q = nq
    7) check
        for i in range(0, numCourses):
            if indegree[i] != 0:
                return False
4. Summarize
        # 진입차수 
        indegree = [0] * (v + 1)
        # 그래프 
        graph = collections.defaultdict(list)
        
        # 그래프, 진입차수 init
        for x, y in prerequisites:
            graph[x].append(y)
            indegree[y] += 1 # 진입차수 
        q = []
        
        for i in range(0, numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            nq = []
            for now in q:
                for i in graph[now]:
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        nq.append(i)
            q = nq
        for i in range(0, numCourses):
            if indegree[i] != 0:
                return False
        return True
            
            

'''