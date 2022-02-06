# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        answer = 0
        
        while q:
            answer = q[0]
            
            nq =[]
            
            for n in q:
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            
            q = nq
        
        return answer.val 
        
        
        
        
'''
        q = [root]
        answer = 0
        while q:
        
            answer = q[0]
            
            nq = []
            // nq
            for n in q:
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            q = nq
        
        return answer


1. Problem is..?
    - bottom , left 
    - tree is not nullable
    
2. TC
    
    tc1)
            1
    
    tc2)
            1
           /
          2
    tc3)
            1
             \
               2
    tc4)
            1
           / \
          2   3
           \
            4
    return      : 4
    
    tc5)
            1
           / \
          2   3
         / \
        4   5
    return      : 4

3. Brain Storming
    a) BFS
        q       : visit now
        nq      : visit next
        
        q = [root]
        answer = 0
        while q:
        
            answer = q[0]
            
            nq = []
            // nq
            for n in q:
                if n.left:
                    nq.append(n.left)
                if n.right:
                    nq.append(n.right)
            q = nq
        
        return answer
            
    b) nq
        q       : [7]
    
    tc1)
        1
        
    q       : []
    nq      : []
    answer  : 1
    
    tc2)
            1
           /
          2
    q       : []
    nq      : 
    answer  : 2
    
4. Summarize

        
        
            
      
    
'''