class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, dic = list(), dict()
        for n in nums2:
            while stack and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)
        
        res = []
        for n in nums1:
            if n in dic:
                res.append(dic[n])
            else:
                res.append(-1)
        return res
        
'''

        for n in nums2:
            while stack and stack[-1] < n:
                temp = stack.pop()
                dic[temp] = n
            stack.append(n)
            

        res = []
        for n in nums1:
            if n in dic:
                res.append(dic[n])
            else:
                res.append(-1)
                
                        ----------------->
                                         n
        nums2          : [5, 4, 3, 2, 1, 6]
        
                        <---------------
        stack          : []
        dic            : {}             
        
        
        O(n)        = O(2n)
        
                                      n
                                   ------->
                       --------->
        nums2       : [5, 4, 3, 1, 6, 7, 8]
                                <-
                       <-------
        stack       : [5, 4, 3]
        
        
        O(2n)
        
                
stack
    a) pair (짝짓기)
    b) inc, dec(오름차순, 내림차순)


1. Problem
    - next greater element 
    - first greater element to right
    - arr       
            nums1       : subset of nums2
            nums2
    - find the index j such that
        nums1[i] == nums2[j]
        
    - array ans
    
    My question
    a) subset ???
    b) same element ??? => unique
    c) empty? >= 1
    d) positive integer
    
2. TCs
    tc1)
    nums1       : [4, 1, 2]
                : [x, 3, x]
    nums2       : [1, 3, 4, 2]
                : [3, 4, x, x]
                
                
    tc2)
    nums1       : [2, 4]
        
    nums2       : [1, 2, 3, 4]
                : [2, 3, 4, x]
    res         : [3, -1]
    
    
    
    tc3)
    nums1       : [1, 2, 3]
    nums2       : [1, 2, 3]
    res         : [2, 3, -1]
    
    
    
    tc4)
    nums1       : [3, 1]
    nums2       : [3, 1, 2]
                : [x, 2, x]
                
                : [-1, 2]
    
3. Brain Storming
    
    a) for loop nums2
    b) find next greater element!!!
        save to dictionary
    c) finally update ans, with nums1
            with for loop
    
    
                              n
    nums2       : [3, 1, 2]
                : [x, 2, x]
    stack       : [3]                <= decreasing ???
    
  
    
                               n
    nums2       : [3, 4, 2, 1, 5]
    stack       : []                        <= decreasing
    tmp         : 4

    
    dic         : {3:4, 1:5, 2:5, 4:5}
    
    
                      n
    nums1       : [3, 5]
    res         : [4, -1]
    
    
    
    
        for n in nums2:
            whilt stack[-1] < n:
                temp = stack.pop()
                dic[temp] = n
            stack.append(n)
            

        res = []
        for n in nums1:
            if n in dic:
                res.append(dic[n])
            else:
                res.append(-1)
'''