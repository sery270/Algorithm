# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        len1 = len2 = 0
        p1 = l1
        p2 = l2
        n = 0 

        while p1:
            p1 = p1.next
            len1 = len1+1
        while p2:
            p2 = p2.next
            len2 = len2+1

        if len1 < len2:
            tmp = l1
            l1 = l2
            l2 = tmp
            n = len2 - len1
        else:
            n = len1 - len2

        p1 = l1
        p2 = l2
        c = l1

        for i in range(n):
            p1 = p1.next

        while p1:
            rest = (p1.val + p2.val)%10
            carrige = (p1.val + p2.val)//10

            p1.val = rest

            if c:
                for i in range(n-1):
                    c = c.next
                c.val = c.val + carrige
                carrige = 0

            p1 = p1.next
            p2 = p2.next
            n = n+1
            
        # print(l1)
        return l1 




        

'''
1. Problem is...?
    a) each list -> digit
    b) non emtpy/ non negative -> 0 ~ 9 
    c) 0 > 1 > 2 > None (x)
    d) singly-linked list
    
2. TC
    tc1)
    1 > 2 > None
        1 > None
    --------------
    1 > 3 > None
        
    tc2)
    0 > None
    1 > 3 > None
    --------------
    1 > 3 > None
    
    tc3)
    1 > 3 > None
    9 > None
    ---------------
    2 > 2 > None
    
    
    tc4)    
    2 > 1 > 3 > None
    8 > 9 > None
    ---------------
    3 > 0 > 2 > None
    
3. Brain Stroming

    l1 >= l2
    
    tc3) 
    
    carriage(c) = 1
    
    a2  
        a1
    2 > 2 > None
    
    b1
    9 > None
    
    an.val + bn.val + c
    
    tc4)
    c = 1
    n = 2
    
    c
            a
    2 > 0 > 2 > None
    
        b
    8 > 9 > None
    
    
    
    

4. Summarize
    l1 >= l2
    
    len1 = len2 = 0
    p1 = l1
    p2 = l2
    n = 0 
    
    while p1:
        p1 = p1.next
        len1 = len1+1
    while p2:
        p2 = p2.next
        len2 = len2+1
    
    if len1 < len2:
        tmp = l1
        l1 = l2
        l2 = tmp
        n = len2 - len1
    else:
        n = len1 - len2
        
    p1 = l1
    p2 = l2
    c = l1
    
    for i in range(n):
        p1 = p1.next
    
    while p1:
        rest = (p1.val + p2.val)%10
        carrige = (p1.val + p2.val)//10
        
        p1.val = rest
        
        if c:
            for i in range(n-1):
                c = c.next
            c.val = c.val + carrige
            carrige = 0
            
        p1 = p1.next
        p2 = p2.next
        n = n+1
        

    
        

'''