# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, p1: ListNode, p2: ListNode) -> ListNode:
        d = ListNode(-1) 
        c = d 
        while p1 and p2:
            if p1.val > p2.val:
                c.next = p2
                p2 = p2.next
            else:
                c.next = p1
                p1 = p1.next
            c = c.next
        c.next = p1 if p1 else p2
        return d.next 
        
        
        
'''
d = ListNode(-1) 
while p1 and p2:
    if p1.val > p2.val:
        c.next = p2
        p2 = p2.next
    else:
        c.next = p1
        p1 = p1.next
    c = c.next
c.next = p1 if p1 else p2
return d.next 
1. 
    a) 두 리스트를 합쳐서 정렬
    b) 공간복잡도 O(1)
    c) 두 리스트는 오름차순 정렬 

2. 
    tc1)
    l1) 1 > 2 > None
    l2) 1 > 2 > None
    ------------------------
    1 > 1 > 2 > 2 > None
    
    tc2)
    l1) 1 > None
    l2) 1 > 2 > None
    ------------------------
    1 > 1 > 2 > None
    
    tc3)
    l1) None
    l2) 1 > None
    ------------------------
    1 > None
    
    tc4)
    l1) None
    l2) None
    ------------------------
    None


3. 
                c    p1
            2 > 3 > None       
d------\    /
        |---
        1   4 > None
            p2
        
        
d = ListNode(-1) 
while p1 and p2:
    if p1.val > p2.val:
        c.next = p2
        p2 = p2.next
    else:
        c.next = p1
        p1 = p1.next
    c = c.next
c.next = p1 if p1 else p2
return d.next 

    

    
    
    
'''