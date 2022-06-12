class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        mem = [0] * (n+1)
        mem[1] = 1
        mem[2] = 2

        for i in range(3, n+1):
            mem[i] = mem[i-1] + mem[i-2]
            
        return mem[n]
        
        
'''
1. Problem
    - stair
    - at once 1 step or 2
    - how many distinct way ?
    
2. TC
    tc1)
        n       : 1
        res     : 1
    
    tc2)
        n       : 2
        res     : 2
    
    tc3)
        n       : 3
        res     : 3
    
        111
        12
        21
        
    tc4)
        n       : 4
        res     : 4
        
        1111
        211
        121
        
        112
        22
        
3. Brain STorming
    - relations
        tc4)
        n       : 4
        res     : 4
        
        111+1
        21+1
        12+1
        => S(3) + 1
        
        11+2
        2+2
        => S(2)+2
        
    S(N) = S(before(1 step)) + S(before(2 step))
    
    mem[n] = mem[n-1] + mem[n-2]
    
    - edge case
        n = 1
        mem[1] = 1
        n = 2
        mem[2] = 2
        
        
4. Summarize
    mem = [0] * (n+1)
    mem[1] = 1
    mem[2] = 2
    
    for i in range(3, n):
        mem[n] = mem[n-1] + mem[n-2]
    return mem[n]
        
    
    
        

    
    
        
        


'''