class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf for _ in range(amount)]
        for i in range(1, len(dp)):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != math.inf else -1
        
'''

    amount  : 3
    
    res     : 2     (2+1), (1+1+1)
    
    
                  c
    coins   : [1, 2]
                        i
               0. 1. 2. 3
    dp      : [0, 1, 1, 2]
    
            
            
1. DP
    => 4 ways
    a) fibonacci
    - 
    
    
    b) state machine
    c) 2 strings
    d) merge intervals (gaps)\
    
    
1. Problem is
    - coins
    - amount
    - total amount of money
    - impossible        : -1
    
2. TC
    tc1)
    conis   : [1, 2]
    amo     : 5
    res     : 3     (2 + 2 + 1)
    
    
    tc2)
    coins   : [1]
    amo     : 5
    res     : 5
    
    tc3)
    coins   : [2]
    amo     : 3
    res     : -1
    
    
    tc4)
    coins   : [1, 2]
    amo     : 3
    res     : 2
    
    tc5)
    coins   : [2, 3]
    amo     : 5
    res     : 2
    
    
3. Brain Storming
    
    amo     : 5
    res     : 2
    
    
    coins   : [1, 2, 3]
    0       : 0
    1       : 1
    2       : 1
                (1 + 1)
                (2)
    3       : 1
    4       : 2
                           c
    5       : 2         <= 1 + (4)      : (4) + 1
                           2 + (3)      : (3) + 1
                           3 + (2)      : (2) + 1       => 2
                           
                           
                           
        
    
    a) dp   <= [0 for _ in range(amount)]?
    b) for c in coins:
         
    
    
    for i in range(1, amoun+1) ??
        for c in coins:
            if i-c is possiblE
            dp[i] = min(dp[i], dp[i-c]+1)
            
            
            
                  c
    coins   : [2, 3]
    amo     : 5
    res     : 2
    
                              i
               0. 1. 2. 3. 4  5
    dp      : [0, i, 1, 1, 2, 2]
                              \
                               \-------dp[3] + 1
                                       dp[2] + 1
                             
    amount      4
                2 + amount(2)
    

'''