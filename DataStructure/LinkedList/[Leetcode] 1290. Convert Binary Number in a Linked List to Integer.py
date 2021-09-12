# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        mlist = head
        cnt = 0
        while True:
            next = mlist.next
            cnt = cnt + 1
            if next == None:
                break
            mlist = next
            
        mlist = head
        sum = 0
        for i in range (cnt-1, -1, -1):
            val = mlist.val
            next = mlist.next
            sum = sum + (2**(i))*val
            if next == None:
                break
            mlist = next
            
        return sum
    
        
        
        
        
'''
5. 
    [1,1,1]
    
    
    next : [1,1]
    cnt : 1
    
    next : [1]
    cnt : 2
    
    next : None
    cnt : 3
    
    i == 2
    
    val : 1
    next : [1,1]
    sum : 0 + 2^2 = 4
    
    i == 1
    
    val : 1
    next : [1]
    sum : 4 + 2^1 = 6
    
    i == 0 
    
    val : 1
    next : None
    sum : 6 + 2^0 = 7


1. 
    시작이 끝 쪽부터 ?

2. 
    [1,1,1] -> 2^2 + 2^1 + 2^0 = 4 + 2 + 1 = 7

3.
     ㅣ = 리스트의 길이
    [1,1,1] -> 2^(ㅣ-1) + 2^(ㅣ-2) + 2^(ㅣ-3) = 4 + 2 + 1 = 7

4.
    - 리스트의 길이를 파악하기
        mlist = head
        cnt = 0
        while True:
            next = mlist.next
            cnt = cnt + 1
            if next == None:
                break
            mlist = next
            
    - sum 구하기 
        mlist = head
        sum = 0
        for i in range(cnt-1, -1, -1)
            val = mlist.val
            next = mlist.next
            sum = sum + (2**(i))*val
            if next == None:
                break
            mlist = next
            

5.



'''