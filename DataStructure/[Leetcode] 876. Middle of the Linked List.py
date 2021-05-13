# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        mlist  = head
        count = 0 
        
        while True:
            nextnode = mlist.next
            count = count + 1
            if nextnode == None:
                break
            mlist = nextnode
        
        mlist = head
        for i in range(count//2):
            mlist = mlist.next
        
        return mlist
    
'''
1. problem is
- 중복되는 숫자가 들어갈 수 있나요, 수열인가요, 정렬여부 (궁금하지만, 문제와 그닥 상관은 없다) no, 문제를 푸는데 고려사항이 아님 위치만 고려해야함
- 노드의 개수는 100개 이하
- 예제를 보면 head노드가 가리키는 노드는 1인건가요 yes

{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}} 
 
2. TC
TC1) [1,2,3,4,5] :: head -> 1 -> 2 -> 3 -> 4 -> 5 -> none
    
    head is pointing
    
    List    : ListNode{val: 1, next: ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}} 
    val     : 1
    next    : ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
    
    
    head.next (val = 1) is pointing     
    
    List    : ListNode{val: 2, next: ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}}
    val     : 2
    next    : ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}
    
    head.next.next (val = 2) is pointing    
    
    List    : ListNode{val: 3, next: ListNode{val: 4, next: ListNode{val: 5, next: None}}}
    val     : 3
    next    : ListNode{val: 4, next: ListNode{val: 5, next: None}}
    
    head.next.next.next (val = 3) is pointing     
    
    List    : ListNode{val: 4, next: ListNode{val: 5, next: None}}
    val     : 4
    next    : ListNode{val: 5, next: None}
    
    head.next.next.next.next (val = 4) is pointing     
    
    List    : ListNode{val: 5, next: None}
    val     : 5
    next    : None
    
    
    ====================================================================

    until next is None, 5 visits (h,1,2,3,4), same as list's length
    
    middle node is 3 node, at third visit's node is pointing 3 node 
    
        so, at second visit's node's next (2 node's next) shoould be returned
    
    
TC2) [1,2] :: head -> 1 -> 2 -> none
    
    middle node is 2 node, at second visit's node is pointing 2 node 
    
        so, at first visit's node's next (1 node's next) shoould be returned

    
    
3. brain stroming
    a) cal linked list's length
         until next node is none, keep visit the next node and count the visits (from head to last node)
            so, if the list's length is N, the count is N + 1
        
        list  = head
        count = 0 
        for val, nextnode in list:
            count = count + 1 # representing the node index (starts 1) and last index would be same as list's length
            if nextnode == None:
                break
            list = nextnode
            
        
        
    b) visit middle node
        when linked list's length (N)
            -> even {middle node is that (N//2) visit's node is pointing }
            -> else {middle node is that (N//2)+1 visit's node is pointing }

4. summarize

        mlist  = head
        count = 0 
        visit = 0
        for val, nextnode in mlist:
            count = count + 1 # representing the node index (starts 1) and last index would be same as list's length
            if nextnode == None:
                break
            mlist = nextnode
        
        if count%2:
            visit = count//2 + 1
        else:
            visit = count//2 
            
        mlist = head
        for i in range(visit):
            mlist = mlist.next
        
        return mlist
    
'''    

