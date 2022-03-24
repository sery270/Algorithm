import string
import math

tmp = string.digits+string.ascii_lowercase

def solution(n, k):
    res = []
    nk_list = str(n_to_nk(n,k)).split("0")
    # print(nk_list)
    while '' in nk_list:
        nk_list.remove('') 
    while '1' in nk_list:
        nk_list.remove('1') 
    for nk in nk_list:
        if is_prime_number(int(nk)):
            res.append(nk)
    return len(res)
    


def n_to_nk(n, k) :
    q, r = divmod(n, k)
    if q == 0 :
        return tmp[r] 
    else :
        return n_to_nk(q, k) + tmp[r]
    
def is_prime_number(x):
    for i in range (2, int(math.sqrt(x) + 1)):
        if x % i == 0:	
        	return False
    return True			
'''
~19:25
1. Problem is..?

2. TC
    tc1)
        
        n       : 1
        k       : 10
        ===============
        res     : 1
    
    tc2)
        n       : 11
        k       : 10
        ===============
        res     : 1
        
    tc3)
        n       : 12
        k       : 10
        ===============
        res     : 0
    tc4)
        n       : 11 
        k       : 10
        ===============
        100101
        res     : 1

3. Brain Storming
    - k진수 변환 => def n_to_nk()
        nk_list = str(n_to_nk(n,k)).split(0)
    - 조건 맞는 수 확인 => split(0)
        211020101011
        [211 2 1 1 11] => 
        110011
        [11 11]
        11
        [11]
        1
        [1]
        3010410200
        [3 1 41 2] 
            
        
        
    - 소수 확인 => is_prime_number
        res = []
        for nk in nk_list:
            if is_prime_number(nk):
                res.append(nk)
                
                
4. Summarize
    nk_list = str(n_to_nk(n,k)).split(0)
    res = []
    for nk in nk_list:
        if is_prime_number(nk):
            res.append(nk)
    return len(res)
            
        



'''