class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        if l == r and nums[l] == target: 
            return [0,0]
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                while l <= r:
                    if nums[l] < target:
                        l = l+1
                    if nums[r] > target:
                        r = r-1
                    if nums[l] == nums[r] == target:
                        break
                return [l,r]
            if nums[m] > target:
                r = m-1
            if nums[m] < target:
                l = m+1
        return [-1,-1]
                 

        
        
'''
-1. Question
    1. = 의 유무 ?
    2. 
                               m 
                               r
                             l
        nums        : [5,7,7,8,8,10]
        target      : 8
        ==========================
        res         : [3,4]
        
        
        

0. test
    l,r = 0, len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            while l<=r:
                if nums[l] < target:
                    l = l+1
                if nums[r] > target:             
                    r = r-1
            return [l,r]
        if nums[m] > target:
            r = m-1
        if nums[m] < target:
            l = m+1
    return [-1,-1]
1. Problem is...?
    a) sorted array -> 1,2,3,,,,max
    b) elements -> not distinct
    c) time complexity -> O(log n)
    d) return [target's start ix, target's end ix]
    
2. TC
    tc1)
        nums        : [1,1,2,3]
        target      : 1
        =======================
        res         : [0,1]
    
    tc2) 
        nums        : [1,1,2,3]
        target      : 2
        ========================
        res         : [2,2]
        
    tc3)
        nums        : [1,1,2,3]
        target      : 4
        =======================
        res         : [-1,-1]
    
    tc4)
        nums        : []
        target      : 0
        =========================
        res         : [-1,-1]
        
3. Brain Storming
    a) O(log n) search algorithm -> binary search
                         
                           m
                             r
                         l   
        nums        : [0,1,1,1,3]
        target      : 1
        =======================
        res         : [1,3]    
        
        
        
                           m
                           r
                           l
        nums        : [1,1,2,3]
        target      : 2
        ========================
        res         : [2,2]
        
        m = (l+r)//2
        if nums[m] == target:
            if nums[l] < target:
                l = l+1
            if nums[r] > target:             
                r = r-1
        if nums[m] > target:
            r = m-1
        if nums[m] < target:
            l = m+1
            
    b) if nums[m] == target:

4. Summarize
    
    l,r = 0, len(nums)-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            while l<=r:
                if nums[l] < target:
                    l = l+1
                if nums[r] > target:             
                    r = r-1
            return [l,r]
        if nums[m] > target:
            r = m-1
        if nums[m] < target:
            l = m+1
    return [-1,-1]



'''