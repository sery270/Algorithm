'''
나의 풀이 
'''

# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
        
#         answer = 0
#         # example 1 > "011"과 "123"
#         num_len = max(len(num1),len(num2))
#         num1 = num1.zfill(num_len)
#         num2 = num2.zfill(num_len)
        
#         cnt = num_len - 1
#         for i in range(0, num_len):
#             answer = answer + (int(num1[i]) + int(num2[i]) ) * (10 ** cnt)
#             cnt = cnt - 1

#         return str(answer)

'''
교수님의 풀이와 피드백  
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1
           
        diff = len(num1) - len(num2)
        res, carry = '', 0
       
        for i in range(len(num1)-1, -1, -1):
            if i >= diff:
                temp = int(num1[i]) + int(num2[i-diff]) + carry
            else:
                temp = int(num1[i]) + carry
            res = str(temp % 10) + res
            carry = temp // 10
           
        if carry > 0:
            res = str(carry) + res
        return res
       
'''
                  01
                 i
    num1        : 99
    num2        : 2
    -----------------
    res         : '101'
    carry       : 1
   
    temp        : 10
   
    diff        : 1
   
   

1) Problem is  (My question ??!!)
    a) given two non-negative integers
    b) negative ?? 0 ?? Positive ???
    c) int convert ??? str ?????
    d) return the sum ===> string ?? int ????
    e)
   
   
2) TC   <= make it smalller
   
    tc1)
    num1        : 11
    num2        : 23
    res         : 34
   
   
    tc2)
    num1        : 1
    num2        : 9
    res         : 10
   
   
    tc3)
    num1        : 0
    num2        : 9
    res         : 9
   
   
    tc4)
    num1        : 99
    num2        : 2
    res         : 101
   
   
3) Brain Storming
   
                  1
    num1        : 99
    num2        :  2
    -----------------
    res         :101
   
   
                 i
    num1        : 92
    num2        :  9
    ------------------
    res         : '01'            <- res = str(temp % 10) + res
   
    temp        : 10            <- int(num1[i]) + int(num2[i]) + carry  <= if i >= diff
                                  int(num1[i]) + carry
    carry       : 1             <- temp % 10
   
   
   
    str(carry) + res   after for loop !!!
   
    return res
   
   
4) Summarize my idea

    for loop reversely !!!
        if i >= diff:
            temp = int(num1[i]) + int(num2[i]) + carry
        else:
            temp = int(num1[i]) + carry
       
        res = str(temp % 10) + res
    if carry > 0:
        res = str(carry) + res
    return res
   
    diff        : len(num1) - len(num2)
   


'''