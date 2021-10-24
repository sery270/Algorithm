# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        
        while l<=r:
            m = l+(r-l)//2
            if isBadVersion(m):
                if m == 1 or not isBadVersion(m-1):
                    return m    
                r = m-1
                # if m > 1 and isBadVersion(m-1):
                #     r = m-1
                # else:
                #     return m
            else:
                l = m+1
                
        """
        :type n: int
        :rtype: int
        """
        
'''
0. Test
    
    tc2)
    n       : 1
    bad     : 1
    res     : 1
    
    
     l
     r
     m
    [1]
    [T]
        
        



1. Problem is ?
    a) find first bad version
    b) 1,,,n 
    c) binary search
  
2. TC
    tc1)
    n       : 3
    bad     : 2
    res     : 2
    
    tc2)
    n       : 1
    bad     : 1
    res     : 1
    
    tc3)
    n       : 5
    bad     : 4
    res     : 4

3. Brain Storming
    a) isBadVersion
        
             
                 r
               l
               m
         1 2 3 4 5 
        [F,F,F,T,T]
        
        
        m = l + (r-l)//2
        T       : r = m-1 -> if m is not first
                : 
        F       : l = m+1
        
    b) binary search
        while l <= r:

    c) how to check first version 
        if isBadVersion(m-1):
            r = m-1 
        else:
            return m

4. Summarize
    
    while l <= r:
        m = l+(r-l)//2
        if isBadVersion(m):
            if isBadVersion(m-1):
                r = m-1
            else:
                return m 
        else:
            l = m+1
        
    
    
'''