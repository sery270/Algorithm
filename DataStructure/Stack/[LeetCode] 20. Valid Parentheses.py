class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{':'}', '(':')', '[':']'}
        st = deque([])
        for c in s:
            if c in brackets.keys(): # opening
                st.append(c)
            else: # closing
                if not st:
                    return False
                if c == brackets[st.pop()]:
                    continue
                return False
        if st:
            return False
        return True 
                
        
'''
1. Problem 
    - open and close
    - an input str is valid if
        - open brackets must be closed by the same type of brackets
    
2. TC
    tc1)
        s       : ()
        res     : T
        
    tc2)
        s       : ([])
        res     : T
        
    tc3) 
        s       : (
        res     : F
    
    tc4)
        s       : (){}
        res     : T
    
    tc5)
        s       : (}
        res     : F
        
3. Brain Storming
    tc1)
                  i  
        s       : ()
        res     : T
        
        s       : ([)]
        res     : F
        
        a) FIFO -> ST
            현재 닫힌 괄호 등장 
            가장 최근의 열린 괄호를 검사
            st = []
            
            [ ( -> appendleft()
            
            ) -> pop()
            
        b) 
        
        opening 
            => stack
        closing 
            => comparing : pop elements
            
                    
        
        

'''
        