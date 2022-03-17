# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []

        
        
        
        
'''
        if root:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        else:
            return []
            
        answer = []
        
        def helper(self, root)
            if not root:
                return 
            self.helper(root.left)
            answer.append(root.val)
            self.helper(root.right)
            return 

0923
1. Problem is..?
    a) inorder : left root right
    b) binary tree
    
2. TC
    tc1) 
            1
           /
          1
    res : 1 1
    
    tc2)
            1
    res : 1
    
    tc3)
            None
    res : None
    
    tc4)
            1
           /
          2
         /
        3
    res : 3 2 1
    
    tc5)
    
            1
           / \
          2   3
    res : 2 1 3
    
    tc6)
    
            1
             \
              2
             /
            3
    res : 1 3 2
    
3. Brain Storming
    a) recursive
        answer = []
        
        def helper(self, root)
            if not root:
                return 
            self.helper(root.left)
            answer.append(root.val)
            self.helper(root.right)
            return 
    
    b) return ? 
        answer 
    c) edge case 
    tc3)
            None
    res : None
    
    tc2)
            1
    res : 1
    
                        (1n, [1]) 
                        /           \   
                (None, []]) R       (None, [1]) R
                
                
    tc5)
    
            1
           / \
          2   3
    res : 2 1 3
    
    
                        (1n,[2,1]) L65
                        /               \
                (2n, [2]) R             (3n, [2,1,3]) R
                /           \
            (None, []) R    (None, []) R    
    
    
            
            
        
    
                
            
'''