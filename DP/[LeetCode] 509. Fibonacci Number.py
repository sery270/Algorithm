class Solution:
    def fib(self, n: int) -> int:
        if n < 2: 
            return n
        prev2 = 0
        prev = 1
        now = 0
        for i in range(2,n+1): # n+1-2
            # mem F(2) ~ F(n-1) 
            now = prev + prev2

        return now
    
        
        
'''
0 .test
    n       : 3
    
                   i
               0 1 2
    mem     : [0,1,1]
    
    F(n) = F(n-1) + F(n-2) 
    now    prev  + prev2
            
    
    

            

1. problem 
    - fibo 
        - F(n) = F(n-1) + F(n-2) 
        - F(0) = 0 / F(1)= 1 
        
2. TC
    tc1)
        n       : 0
        res     : 0
        
    tc2)
        n       : 1
        res     : 1
    
    tc3)
        n       : 2
        res     : F(0) + F(1) = 0 + 1 = 1
        
    tc4) 
        n       : 3
        res     : F(1) + F(2) = 1 + 1 = 2
        
        
3. brain storming

    F(n) = F(n-1) + F(n-2) 
    
    0-n
    
    tc4) 
        n       : 3
        
        F(0), F(1), F(2)
        
    
    tc5)
        n       : 5
        F(0), F(1), F(2), F(3), F(4), F(5)
        
    
    mem = [-1] * n
    mem[0] = 0
    mem[1] = 1
    for i in range(2,n):
        # mem F(2) ~ F(n-1) 
        mem[i] = mem[i-1] + mem[i-2]
    
    return mem[n-1] + mem[n-2]
    
    
        
        
    
        

'''
        