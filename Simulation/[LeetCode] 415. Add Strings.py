class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        answer = 0
        # example 1 > "011"과 "123"
        num_len = max(len(num1),len(num2))
        num1 = num1.zfill(num_len)
        num2 = num2.zfill(num_len)
        
        cnt = num_len - 1
        for i in range(0, num_len):
            answer = answer + (int(num1[i]) + int(num2[i]) ) * (10 ** cnt)
            cnt = cnt - 1

        return str(answer)
        
       