class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        
        while l<r:
            if numbers[l] + numbers[r] > target:
                r = r-1 
            elif numbers[l] + numbers[r] < target:
                l = l+1
            else:
                return [l+1, r+1]
        
        
'''
        l, r = 0, len(numbers)-1
        
        while l<r:
            if numbers[l] + numbers[r] > target:
                r = r-1 
            elif numbers[l] + numbers[r] < target:
                l = l+1
            else:
                return [l+1, r+1]
                
1. Problem is?
    a) numbers에서 2가지 원소 합 == target 
    b) index가 1부터 시작 
    c) 오름차순 정렬
    
2. TC
    tc1)
    numbers     : [2,2]
    target      : 4
    =====================
    answer      : [1,2]
    
    tc2) 
    numbers     : [1,2,3]
    target      : 4
    ======================
    answer      : [1,3]
    
    tc3)
    numbers     : [0,1]
    target      : 1
    answer      : [1,2]
    
3. Brain Storming
    tc2) 
                     r             
                   l
                   0 1 2 
    numbers     : [1,2,3]
    target      : 3
    ======================
    answer      : [1,2]
    
    a) two pointer 
        l, r = 0, len(numbers)-1
        
        while l<r:
            if numbers[l] + numbers[r] > target:
                r = r-1 
            elif numbers[l] + numbers[r] < target:
                l = l+1
            else:
                return [l+1, r+1]
    
    
    
    

'''