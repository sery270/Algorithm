class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        st = deque([])
        
        for c in s:
            if c == '(': # opening
                st.append(c)
            else: # closing
                if not st:
                    cnt += 1
                    continue
                if c == ')':
                    st.pop()
                    continue
                cnt += 1
        while st:
            cnt += 1
            st.pop()
        return cnt  
        

'''
1. Problem 
    - make parenthese valid to add string 
    - count required char 
    
2. TC
    tc1) 
        s       : "("
        res     : 1
        
    tc2) 
        s       : ")"
        res     : 1
    
    tc3) 
        s       : "()"
        res     : 0
    
    tc4) 
        s       : ")("
        res     : 2
    
    tc5) 
        s       : "(())"
        res     : 0
        
        
3. Braing Storming
    - validation
    
        brackets = {'{':'}', '(':')', '[':']'}
        st = deque([])
        for c in s:
            if c in brackets.keys(): # opening
                st.append(c)
            else: # closing
                if not st:
                    cnt++ 
                if c == brackets[st.pop()]:
                    continue
                cnt++ 
        while not st:
            cnt++ 
        return cnt         
        
    - moves 
        cnt = 0
        


'''