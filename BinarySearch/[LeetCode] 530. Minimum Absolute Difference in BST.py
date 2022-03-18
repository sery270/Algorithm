# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def min(self, a, b) -> int:
        if a > b:
            return b
        else:
            return a

    def inorder(self, root) -> List[int]:
        if root:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
        else:
            return []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inordered = self.inorder(root)
        
        tmp = 1000000
        
        for i in range(len(inordered)-1):
            tmp = min(tmp,inordered[i+1]-inordered[i])
        
        return tmp
        
        
'''
                
        inordered = []
        tmp = 1000000
        for i in range(len(inordered)-1):
            tmp = min(tmp, inordered[i+1]-inordered[i])
        return tmp
1. Problem is..?
    - bst 
        => sorted => search order
    - the minimum absolute difference between the values
    - tree is not nullable
    
2. TC
        
tc1)

[236,104,701,null,227,null,911]


                236
          /             \
        104             701
            \               \
            227             911
            
    bst => sorted
    inorder => 104 227 236 701 911 
res : 9

tc2)
        0
            \
            100000
            
    res : 100000
    
tc3)
            2
        /       \
    1               3
    res : 1
    
tc3)
            5
        /       \
    1               6
                  /
               4
    res : 1
    inorder => 1 5 4 6

3. Brain Storming
    BST => sorted !! => search order !! 
    
    a) inorder
        def inorder(self, root) -> List[int]:
            if root:
                return self.inorder(root.left) + [root.val] + self.inorder(root.right)
            else: 
                return []
                
        inordered = []
        tmp = 1000000
        for i in range(len(inordered)-1):
            tmp = min(tmp, inordered[i+1]-inordered[i])
        return tmp
            
    b) find diff  
    
4. Summarize

def min(self, a, b) -> int:
    if a > b:
        return b
    else:
        return a

def inorder(self, root) -> List[int]:
    if root:
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
    else:
        return []


    
    
        
    
'''