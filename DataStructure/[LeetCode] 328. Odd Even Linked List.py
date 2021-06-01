# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
       
        o = os = head
        e = es = head.next
       
        while e and e.next:
            on, en = o.next.next, e.next.next
            o.next = on
            e.next = en
            o, e = on, en
           
        o.next = es
        return os
       
       
'''
    os es
    o
        e
    1 > 2 > None
   
    os es
            o
                e
        |-------\
    1   2 < 3   None
    |------/
   
   


1) Problem is ...
    a) odd left // even right
    b) f    : odd
       s    : even
       
    c) relative order !!
   
2) TC       <= make it smaller !!!
    tc1)
    1 > 2 > 3 > 4 > 5 > None
    1 > 3 > 5 > 2 > 4 > None
   
    tc2)
    1 > 2 > 3 > None
    1 > 3 > 2 > None
   
   
    tc3)
    None
    None
   
   
    tc4)
    1 > None
    1 > None
   
    tc5)
    1 > 2 > None
    1 > 2 > None
   
   
   
   
3) Brain Storming

    h
   
              e
            o  
       
        |-----\
    1   2  3 > 4 > None
    |------/
   
   
    1 > 3
    2 > 4 > None

    o = os = head
    e = es = head.next
   
   
    while e and e.next:
        on, en = o.next.next, e.next.next
        o.next = on
        e.next = en
        o, e = on, en
    o.next = es
    return os
   
   
    p
            c
    1 > 2 > 3 > 4 > None
   
   
    p.next = c
        p      
                c
        1   2 > 3 > 4 > None
        |------/
    c = p.next
        p
            c
        1 > 2 > 3 > 4 > None
   
'''