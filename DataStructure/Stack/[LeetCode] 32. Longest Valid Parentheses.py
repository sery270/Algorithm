class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        res = max(res, i - stack[-1])
                    else:
                        stack.append(i)
        return res
        
        
'''
               i
              01234
    s       : )()()
    st      : [0,]
    
    res     : 0
                
                
    Stack
        a) pairing (짝짖기)
        b) increasing decreasing
        
        
    what should we save into stack?
        a) value
        b) key
        c) both
        
        
    which one should we use from stack?
        a) poped
        b) stack[-1]
        
    dummy
        a) 
        
        
1. Problem
    - (, )
    - find the length of longest valid parenethese
    - i
    
    
    My question
    a) can s have other than () ??
        => no
    b) valid or invalid
    c) 
    
2. TCs
    tc1) 
    s       : (()
    res     : 2
    
    tc2)
    s       : ()()
    res     : 4
    
    
    
3. Brain Storming
        
                i
              012
    s       : ())
    
    stack   : []
    
    
    res     : 2         <= max(res, i - pop's index + 1)
    
    
                 i
              0123
    s       : ()()
    stack   : [2, ]
    
    poped   : 2
    
    res     : 2     
    
    
                 i
              0123
    s       : ()()
    st      : [-1]
    
    res     : 4         <= initialize 0
                        <= max(res, i - i - stack[-1])
                        
                        
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                res = max(res, i - stack[-1])
            
'''