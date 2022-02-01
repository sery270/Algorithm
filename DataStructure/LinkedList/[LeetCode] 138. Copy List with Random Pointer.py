"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 20210201 19:00
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        now = head
        copy_head = Node(now.val)
        copy_now = copy_head
        node_dict = {}
        
        while now:
            if not now.next:
                copy_now.next = None
            else:
                copy_now.next = Node(now.next.val)
                
            node_dict[now] = copy_now
            
            now = now.next
            copy_now = copy_now.next
        
        now = head
        copy_now = copy_head

        node_dict[None] = None
        
        while now:
            copy_now.random = node_dict[now.random]
            
            now = now.next
            copy_now = copy_now.next
            
        return copy_head

        
        
       
        
'''
0. Test
        if !head:
            return None
        
        now = head
        copy_head = Node(now.val)
        copy_now = copy_head
        node_dict = {}
        
        while now:
            // deep copy code : next pointer
            if !now.next:
                copy_now.next = None
            else:
                copy_now.next = Node(now.next.val)
            // dict 
            node_dict[now] = copy_now
            now = now.next
            copy_now = copy_now.next
        
        now = head
        copy_now = copy_head
        while now:
            copy_now.random = node_dict[now.random]
            now = now.next
            copy_now = copy_now.next
        
        return copy_head



1. Problem is...?
    - length n 
    - pointing node or null
    - deep copy 
        - deep copy vs shallow copy 
            : deep copy     : pointing a new addr
            : shallow copy  : pointing a original addr
    - Can random pointer pointing themselves ? Yes
    - Is node's val unique ? No

2. TC 
    
    TC 1)
    head        : [[1,0],[11,1],[2,2]]
    
    TC 2)
    head        : []

    TC 3)
    head        : [[1,0],[1,0]]
    
    TC 4)
    head        : [[100,null]]


3. Brain Storming

    TC 4)
    head        : [[100,null]]
    
    next    : >
    random  : |-\ 
    
     |-----------\    
    100 > None  null

        
        
    TC 1)
    head        : [[1,2],[11,1],[2,2]]
    
    
    
    dict = {1n:1cn,11n:11cn,2n:2cn }
          n
    h   > 1 > 11 > 2
    ch  > 1 > 11 > 2
    
    
    
    
    
    
    
    
    
    1. O(2n) -> O(n)
        - next deep copy
        - random deep copy
    
    
        if !head:
            return None
        
        now = head
        copy_head = Node(now.val)
        copy_now = copy_head
        node_dict = {}
        
        while !now:
            // deep copy code : next pointer
            if !now.next:
                copy_now.next = None
            else:
                copy_now.next = Node(now.next.val)
            // dict 
            node_dict[now] = copy_now
            now = now.next
            copy_now = copy_now.next
        
        now = head
        copy_now = copy_head
        while !now:
            copy_now.random = node_dict[now.random]
            now = now.next
        
        return copy_head
        
        
        
    

4. Summarize

        if !head:
            return None
        
        now = head
        copy_head = Node(now.val)
        copy_now = copy_head
        node_dict = {}
        
        while now:
            // deep copy code : next pointer
            if !now.next:
                copy_now.next = None
            else:
                copy_now.next = Node(now.next.val)
            // dict 
            node_dict[now] = copy_now
            now = now.next
            copy_now = copy_now.next
        
        now = head
        copy_now = copy_head
        while now:
            copy_now.random = node_dict[now.random]
            now = now.next
            copy_now = copy_now.next
        
        return copy_head
        

5. Test





'''
# 20210201 19:12