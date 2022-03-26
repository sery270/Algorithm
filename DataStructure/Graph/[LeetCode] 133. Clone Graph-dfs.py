"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: 
            return None
        if not node.neighbors:
            return Node(node.val)
        
        node_dict = defaultdict()
        
        # copy node
        def dfs(node):
            if node:
                for org in node.neighbors:
                    if not org in node_dict: 
                        node_dict[org] = Node(org.val)
                        dfs(org)
        
        dfs(node)
        
        # copy neighbors
        for org, copy in node_dict.items():
            for n in org.neighbors:
                copy.neighbors.append(node_dict[n]) 
                
        return node_dict[node]


        
'''
1. Problem is
    - BFS
    - undirected
    - finite
    - nullable? yes
    - unique val
    - no self-loops
    - connected : all nodes can be visited 
    
    
2. TC 
    tc1)
        org     : 1n
        copy    : 1'n
        
    tc2)
        org     : None
        copy    : None
        
    tc3)
        org     : 
                    1n
                    / \
                  2n - 3n
        copy    :
                    1'n
                    /  \
                  2'n - 3'n

3. Brain Storming - DFS
    - draw
        
        org     : 
                    1n
                    / \
                  2n - 3n
                  
                  
        dfs)
                    1'n
                    /
                  2'n
                  /
                3'n
    - tree
        def dfs(node);
            if node:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            
    - visited 
        
        node_dict = defaultdict()
        
    - graph
        # copy node
        def dfs(node);
            if node:
                for org in node.neighbors:
                    if not org in node_dict: 
                        node_dict[org] = Node(org.val)
                        dfs(org)
        # copy neighbors

        for org, copy in node_dic.items():
            for n in org.neighbors:
                copy.neighbors.append(node_dic[n]) 

        
                 

'''