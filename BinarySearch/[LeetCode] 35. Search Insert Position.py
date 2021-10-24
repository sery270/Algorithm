class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            if nums[m] < target:
                l = m + 1
        return l
        

        
'''
                           m
                           r
                              l(4)
        nums        : [1,2,3]
        target      : 4
        =====================
        res         : 3
        output      : 2
        
        
        

0. test
        
        l,r = 0, len(nums)-1
    
        while 1 =< r: 
            m = (l+r)//2    
            if nums[m] == target:
                return m
            if num[m] > target:
                r = m - 1 
            if num[m] < target:
                l = m + 1 
            
        return l 
         
1. Problem is..?
    a) elements -> distinct integers 
    b) sorted array -> 1,2,3,,,,,max
    c) time complexity -> O(log n)
    d) return the target's ix || return the ix where it would be 
    
2. TC 
    tc1) 
        
        nums        : [1,2,3]
        target      : 2
        ======================
        res         : 1
        
    
    tc2)
                       0 1 2
        nums        : [1,2,3]
        target      : 4
        =======================
        res         : 3
        
    tc3)
        nums        : [1]
        target      : 1
        =======================
        res         : 0
        
    tc4)
        nums        : [1]
        target      : 0
        ======================
        res         : 0
    
3. Brain Storming
    a) time complexity : O(log n) -> binary search algorithm >< 
        1) compare 3 parts : middle / left/ right -> pointer
                    
                         m
                           r
                       l 
                       0 1 2
        nums        : [1,2,3]
        target      : 1
        ======================
        res         : 1

        comparing muns[m]
            - same
            - less
            - more

        m = (l+r)//2
        if nums[m] == target:
            return m
        if num[m] > target:
            // move left side 
        if num[m] < target
            // move right side 
            
    b) move m pointer
        1) move left side 
            r = m - 1 
            // m update
        2) move right side 
            l = m + 1 
            // m update
            
    c) return the ix where it would be 
        
        ** l, r init**
        
        ** loop or recursion ** 
        m = (l+r)//2
        if nums[m] == target:
            return m
        if num[m] > target:
            r = m - 1 
        if num[m] < target:
            l = m + 1 
         
         l -> left
         r -> right 
         
         if l > r :
            return l 
         => 정상적인 상황이 아님 ! 
         => target이 들어갈 자리를 계산해줘야함 ! 
        
            
            
            
         
         
                           m
                           r
                              l(4)    
                       0 1 2
        nums        : [1,2,3]
        target      : 4
        =======================
        res         : 3
    
            
            

                 
         
                       m
                       r
                         l    
                       0 1 2
        nums        : [1,3,4]
        target      : 2
        =======================
        res         : 1
        
                       m
                       l
                r(-1)
                       0
        nums        : [1]
        target      : 0
        ======================
        res         : 0
        
4. Sumaary
    
    
        l,r = 0, len(nums)-1
    
        while 1 =< r: 
            m = (l+r)//2    
            if nums[m] == target:
                return m
            if num[m] > target:
                r = m - 1 
            if num[m] < target:
                l = m + 1 
            
        return l 
         

    
            
        
'''