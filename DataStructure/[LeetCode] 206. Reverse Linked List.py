# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = None
        while head:
            c = head
            head = head.next
            c.next = p
            p = c
        return p
       
'''
 
a) pointers !!! => (c, p) => NPE
    hn = head.next
b) middle of linked list // cycle
                    f
            s
    1 > 2 > 3 > 4 > None
   
                f
                s
    1 > 2 > 3 > 4 > 5
        ^-----------|
c) dummy
            h
    dummy > 1 > 2 > 3 > 4 > None
   
    dummy = ListNode(-1)
    dummy.next = head

   
   
1) Problem is ... (My question)
    a)  singly linked list !!!      => doubly linked list ???? 1 > 2 > 3 > None /// 3 <> 4 <> 5 <> None
    b) revese d list ??
    c) head is null ??
   
2) TC <= make it smaller !!!!
    tc1)
    input       : 1 > 2 > 3 > None
    res         : 3 > 2 > 1 > None
   
   
    tc2)
    input       : 1 > None
    res         : 1 > None
   
    tc3)
    input       : None
    res         : None
   
    tc4)
    input       : 1 > 2 > None
    res         : 2 > 1 > None
   
   
3) Brain Storming !!! (visualization---->code)
               h
        c
        p
    1 < 2    None
    |---------^
   
p = None
while head:
    c = h
    h = h.next
    c.next = p
    p = c
   
                 h
             c
             p
    1 < 2 < 3   None
    |--------------^
'''
