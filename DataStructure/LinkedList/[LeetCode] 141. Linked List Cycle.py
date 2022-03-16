# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow, fast = head, head.next
        
        if fast != None:
            fast = fast.next
        
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next
            
        return False
            
                
            
        
        

        
        
        
'''
0912
        class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow, fast = head, head.next
        
        
        while fast != None and fast.next != None:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next
            
        return False
        
            s
                    f
        3 > 2 > 0 > -4 
            \--------|
            
            
            s
                f
        3 > 2 > 0 > -4 
            \--------|
0. test

    while True: // fast
        if not fast:
            return false
        while True: // slow 
            if not slow:
                break
            if fast.next == slow:
                return True
            if fast == slow:
                break
            slow = slow.next
            
         fast = fast.next
         slow = head
            

            s
                    f
        3 > 2 > 0 > -4
            \--------|
    
    tc5)
    
        s
        f
        1 
       \-/
    res : true
    
    tc1)
        s
                f
        1 > 2 > 3
        \-------|
        
    res : true
    
    
    tc2)
    
        None
        
    tc3)
                s
                f
        1 > 1 > None
    
    res : false
        
    






        slow = head
        fast = head
        
        while True: // slow
            if not slow:
                return false
            while True: // fast
                if not fast or not fast.next:
                    break
                if fast.next == slow:
                    return true
                fast = fast.next
            slow = slow.next
            
            
            
            
1. Problem is..?
    a) find cycle 
    b) val unique? 
    c) null list
    

2. TC
    tc1)
        
        1 > 2 > 3
        \-------|
        
    res : true
    
    tc2)
    
        None
    res : false
    
    tc3)
    
        1 > 1 > None
    
    res : false
    
    tc4) 
    
        1 > None
    res : false
    
    tc5)
    
        1 
       \-/
    res : true
    
    tc6)
        1 > 2 > 3 > None
        \---|
        
    res : true
    
3. Brain Storming
    a) 
        p   
                np
        1 > 2 > 3
        \-------|
        
        s
            f
        1 > 2 > 3 > None
        \---|
        
        
                s
                f
        1 > 1 > None
        
        
    
    b) slow pointer and fast pointer
        slow -> 기준
        fast -> 비교 대상 
        
        slow = head
        fast = head
        
        while True: // slow
            if not slow:
                return false
            while True: // fast
                if not fast or not fast.next:
                    break
                if fast.next == slow:
                    return true
                fast = fast.next
            slow = slow.next

4. Summarize
        slow = head
        fast = head
        
        while True: // slow
            if not slow:
                return false
            while True: // fast
                if not fast or not fast.next:
                    break
                if fast.next == slow:
                    return true
                fast = fast.next
            slow = slow.next

            
                
                    
        
        
        
        
    
    
    
        
        
    
        
'''