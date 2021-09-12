# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        d = ListNode(val = -1, next = head)

        r = f = s = d 

        for _ in range(n+1) :
            f = f.next

        while f :
            f = f.next
            s = s.next

        s.next = s.next.next
    
        return r.next
        

'''

test) n = 1 

    r
                    f
            s
    d > 1 > 2  3 > None 
            |--------^
            
    

1) problem is
 one pass ? 한 번만 순회 
 n=1 > 맨 마지막 노드  삭제
 sz가 1보다 같거나 크므로, head 로 null 이 오지 않음
 
2) TC

    tc1)
    input : 1 > 2 > 3 > None / n = 2
    res : 1 > 3 > None
    
    tc2)
    input : 1 > 2 > None / n = 2
    res : 2 > None
    
    tc3)
    input : 1 > 2 > None / n = 1
    res : 1 > None
    
3) brain storming

    tc1) n = 2
    
    r
                     f
         s 
    dm > 1  2 > 3 > None
         -------^   
    
    1 > 3 > None
    

    d = ListNode(val = -1, next = head)

    r = d 
    f = d
    s = d
    
    for i in range(n+1) :
        f = f.next
    
    while f :
        f = f.next
        s = s.next
    
    s.next = s.next.nextaa
    
    return s
    
    
    
  tips)
    a) None 확인하기
    b) f,s => cycle dection
    c) f,s,r,d => NPE
    d) 문장의 
    c.next = t
    t = c.next
    
    
'''        