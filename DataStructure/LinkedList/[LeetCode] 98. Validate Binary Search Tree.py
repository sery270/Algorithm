# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, -2**31-1, 2**31)
        
    def helper(self, root, ls, rs):
        if not root:
            return True
        if not ls<root.val<rs:
            return False
        return self.helper(root.left,ls, root.val) and self.helper(root.right, root.val,rs)   
    
'''
1. Problem is...?
    a) valid BST 
    b) 
    
    
    
2. TC
    tc1)
        
        5
       / \
      1   6
         /
        4
    ===============
    res     : false
    
    tc2)
        
        2
       /  \
      1    3
    ================
    res     : True
    
        
    tc2) 
                  7
               /     \
              4       9
             / \     / \  
            3   5   8  10
    ================
    res     : True
        
    tc3)
        1
    ============
    res     : True
        
        
3. Brain Storming
    a) bottom up -> return scale
                        
                        
                        ()
                    /               \
                (min,7)             (7,max)
                /       \           /       \
            (min,4)     (4,7)      (7,9)    (9,max)
            
            
    b) recursion
        
        helper(now, ls, rs):
            if not root:
                return True
            if not ls< root.val <rs:
                return False
            if ls< root.val <rs:
                return self.helper(root.left,ls, root.val) and self.helper(root.right, root.val,rs)
            
    
            helper(root.left,ls, root.val)
            helper(root.right, root.val,rs)
            
4. Summarize
    def helper(root, ls, rs):
        if not root:
            return True
        if not ls<root.val<rs:
            return False
        return self.helper(root.left,ls, root.val) and self.helper(root.right, root.val,rs)    
''' 
        