class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        stack, res = [], [-1 for _ in nums2]
        
        for i in range(len(nums2)):
            while stack and stack[-1][0] < nums2[i]:
                v, k = stack.pop()
                res[k] = nums2[i]
            stack.append((nums2[i], i))
        
        return res[:len(nums)]

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums
        stack, res = [], [-1 for _ in nums2]
        
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                k = stack.pop()
                res[k] = nums2[i]
            stack.append(i)
        
        return res[:len(nums)]
        
        
'''
    nums    : [2, 1]
    
    
                        i
               0. 1. 2. 3
    nums2   : [2, 1, 2, 1]
    stack   : [(2, 0), (1, 3)]
    
               v. k
    poped   : (1, 1)
    
    res     : [-1, 2, -1, -1]

1. Problem 
    - circular integer array nums
    - return NGN
    - greater !! not equal!
    - 
    
2. TCs
    tc1)
        nums        : [1, 2, 1]
        res         : [2, -1, 2]
        
        
    tc2)
        nums        : [1, 2]
        res         : [2, -1]
        
    tc3)
        nums        : [3,  2, 1]
        res         : [-1, 3, 3]
        
        
3) Brain Storming
                       n
        nums        : [1, 2, 1]
        res         : [2, -1, 2]
        
                                   n
        nums        : [1, 2, 1, 1, 2, 1]                <= nums <= nums + nums
        st          : [2, 1, 1, ]
        res         : [2, u, u, u, u, u]
        
        
        
        nums        : [1, 2, 1, 1, 2, 1]
        
        
        
        
        nums        : [20, 10]
        res         : [-1, 2]
        
        
                                    i
                       0.  1.   2. 3
        nums        : [20, 10, 20, 10]
        stack       : [(20, 0), (10, 3)]              <= decreasing to stack??
        
        res         : [u,   20,   u,  u]                  <= [-1 for _ in nums]
        
        
        poped       : (10, 1)
        
        
        
        
        
        
        
        
        nums        : [30,  20, 10]
        res         : [-1,  30, 30]
        
        
        
        nums        : [10, 20, 10, 30]
                                             n
                        0. 1.  2.   3.  4.  5.  6.  7
        nums        : [10, 20, 10, 30, 10, 20, 10, 30]          <= nums + nums
        stack       : [(30, 3)]                        <= save decreasing order
                                                        <= save (val, index)
                                                        <= If we meet greater element,
                                                                let's pop the stack and set res
        
                       v. i
        poped       : (20, 1)
                       0    1   2   3
        res         : [20, 30, 30, -1, 
        
        
        
        while stack and stack[-1][0] < nums[i]:
            v, k = stack.pop()
            res[k] = nums[i]
        stack.append((nums[i], i))
        
        
'''