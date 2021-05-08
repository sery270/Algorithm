import re
from collections import deque

def solution(n, k, cmd):
    answer = ''
    now = k
    now_last = False
    
    # 삭제된 것은 0 아닌 것은 1
    result = [ 1 for _ in range(n) ]
    result_dq = deque([])
    
    d_regex = re.compile("D\s\d+")
    u_regex = re.compile("U\s\d+")
    int_regex = re.compile("\d+")
    
    
    for md in cmd:
        d = d_regex.findall(md)
        u = u_regex.findall(md)
        
        if d:
            x = int_regex.findall(md)
            cnt = 0
            while True:
                if k+1 <= n-1:
                    if result[k+1]:                    
                        cnt = cnt + 1
                k = k+1
                if cnt == int(x[0]):
                    break  
            print(k)
            print(result)
            continue
        if u:
            x = int_regex.findall(md)
            cnt = 0
            while True:
                if k-1 >= 0:
                    if result[k-1]:
                        cnt = cnt + 1
                if cnt == int(x[0]):
                    break
                k = k-1
            print(k)
            print(result)
            continue
        if md == "C":
            if k == n-1:
                result[k] = 0
                result_dq.append(k)
                cnt = 0
                while True:
                    if k-1 >= 0:
                        if result[k-1]:
                            cnt = cnt + 1
                    k = k-1
                    if cnt == 1:
                        break
                    
                print(k)
                print(result)
                continue
            else:
                result[k] = 0
                result_dq.append(k)
                cnt = 0
                while True:
                    if k+1 <= n-1:
                        if result[k+1]:
                            cnt = cnt + 1
                    k = k+1
                    if cnt == 1:
                        break
                    
                print(k)
                print(result)
                continue
        if md == "Z":
            now_z = result_dq.pop()
            result[now_z] = 1
            print(k)
            print(result)
            continue
            



    
    # "U X" 현재 선택된 행에서 X칸 위에 있는 행을 선택
        # 현재행 인덱스 - X
    # "D X" 현재 선택된 행에서 X칸 아래에 있는 행을 선택
        # 현재행 인덱스 + X
    # "C" 현재 선택된 행을 삭제/ 바로 아래 행을 선택, 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
        # 현재행 + 1 ,  현재행 - 1
    
    
    
        # 현재 인덱스 저장 4, 현재 인덱스가 마지막인지 확인 불린 값
        # 현재 행 삭제
        # 불린값이 f면 4로 이동, t면 4-1로 이동
    # "Z" 가장 최근에 삭제된 행을 원래대로 복구/ 현재 선택된 행은 바뀌지 않습니다
        # 최근 삭제된 값 초기화 해둔걸로 복귀 -> 스택에 저장 
    
    
    
    # 약간 인덱스가 아니라 값으로 풀어야할 것 같은데,, 근데 값이 없음 ㅋ
        # 값이야 뭐 만들 수 있음 a초기인덱스 인덱스 이런식으로 
    # "이름"열에는 서로 다른 이름들이 중복없이 채워져 있다고 가정하고 문제를 해결
    for i in result:
        if i:
            answer = answer + 'O'
        else:
            answer = answer + 'X'
            
    return answer
solution(8,2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])