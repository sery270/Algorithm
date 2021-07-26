# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        self.isSubtree(root.left, subRoot) 
        self.isSubtree(root.right, subRoot)
        if root.val != subRoot.val:
            return False
        #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # return (self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right))
        return (self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
'''
0. Test
            3
           / \
          4   5
         /   / 
        1    2
        
            3
           / \
          1   2
    ------------------
    res: False
    
            ist(3n,3nn) L15
            /           
        ist(4n,1nn) 
    
    
    tc1)
            1
           /
          1
          
          1
    ---------------------
    res: True
    
            ist(1n, 1nn) RF
            /       \
    ist(1n, None) RF
    
    =======================
            ist(1n, 1nn) L'
            
            
            
    tc3)
    
            1
           / \
          2   3
         /
        4
        
            2
           /
          4
    -------------------
    res: True
    
            ist(1n,2nn) RT
            /               \
        ist(2n,2nn) RT      
        /              \
    ist(4n,4nn) RT     ist(None,None) RT
    

1. Problem is...?
    a) root, subRoot is not nullable
    b) val is not unique
    c) root can be same with subRoot

2. TC
    tc1)
            1
           /
          1
          
          1
    ---------------------
    res: True
    
    tc2)
            1
           / \
          2   3
          
          1
         /
        2
    -------------------
    res: False
    
    tc3)
    
            1
           / \
          2   3
         /
        4
        
            2
           /
          4
    -------------------
    res: True
    
3. Brain Stroming
    - 수학접 귀납법 접근
    - 아래서부터 리턴 값을 끌고 올라오자. short circuit
        - 항상 조건을 만족시 리턴
    
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False
    if root.val != subRoot.val:
        return False
    return self.

'''
