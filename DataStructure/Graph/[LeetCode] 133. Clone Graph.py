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
        
        # node copy => BFS
        node_dic = defaultdict()
        q = [node]

        while q:
            now = q.pop()
            nq = []
            # nq push
            for org in now.neighbors:
                if not org in node_dic: # visited 
                    node_dic[org] = Node(org.val)
                    nq.append(org)                
            q += nq
            
        # neighbors copy => BFS

        for org, copy in node_dic.items():
            for n in org.neighbors:
                copy.neighbors.append(node_dic[n]) 
                
        return node_dic[node] 
            
        
        
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

3. Brain Storming : BFS
    - draw
        org     : 
                    1n
                    / \
                  2n - 3n
        BFS)
                    1'n
                    / \
                  2'n  3'n
        
        
    - tree sudo
        BFS)
        q       : [2n, 3n]
    
        now     : 2n
        nq      : [1n,3n]
        
            q = [node]
            while q:
                now = q.pop()
                nq = []
                # nq push
                for next in now.neighbors:
                    nq.append(next)
                q.append(nq)
            
    - visited
        {org:copy}
        copy exsist ? visited !!
        
        node_dic = defaultdict()
        if not org in node_dic: 
            node_dic[org] = Node(org.val)
        else:
            # visited => neighbors add
            node_dic[org].neighbors.append()
        
    - graph
            # node copy => BFS
            node_dic = defaultdict()
            q = [node]
            
            while q:
                now = q.pop()
                nq = []
                # nq push
                for org in now.neighbors:
                    if not org in node_dic: # visited 
                        node_dic[org] = Node(org.val)
                        nq.append(org)                
                q += nq
            
            # neighbors copy => BFS
            
            for org, copy in node_dic.items():
                for n in org.neighbors:
                    copy.neighbors.append(node_dic[n]) 
            
            q = [node]
            
            while q:
                now = q.pop()
                nq = []
                # nq push
                for org in now.neighbors:
                
                    if not org in node_dic: # visited 
                        node_dic[org] = Node(org.val)
                        nq.append(org)                
                q += nq   
            

'''
        