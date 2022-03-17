def solution(id_list, report, k):

    answer = []
        
    # 1. 유저가 신고한 id 추출 -> user_report 
    user_report = []
    report_cnt = []

        # tc5)
        # id  : ["a", "b"]
        # rp  : ["a b", "a b", "a b", "a b"]
        # k   : 1
        # res : [1,0]
    for i in range(len(id_list)):
        user_report.append([])
        report_cnt.append(0)
        answer.append(0)
        
    '''
    answer = [0,0]
    user_report = [[],[]]
    report_cnt = [0,0]
    '''

    for rp in report:
        user, reported = rp.split()
        # user_report 중복 제거 해야함 
        try :
            user_report[id_list.index(user)].index(reported) 
        except :
            user_report[id_list.index(user)].append(reported)
            report_cnt[id_list.index(reported)] += 1
            
    '''
    answer = [0,0]
    user_report = [[b,b,b,b],[]]
    report_cnt = [0,4]
    '''        
            
    # 2. 정지된 id 계산 -> blocked 
    blocked = []

    for user in id_list:
        if report_cnt[id_list.index(user)] >= k:
            blocked.append(user)
        
    '''
    answer = [2,0,0]
    user_report = [["b", "c"],[],[]]
    report_cnt = [0,1,1]
    blocked = ["b","c"]
    '''        
        
        
    # 3. user_report와 blocked의 교집합 원소 개수 구하기 
    for i in range(len(id_list)):
        for b in blocked:
            answer[i] += user_report[i].count(b)
            
    return answer


'''
19:56
0. test

        
        
    





1. Problem is...?
    신고
    - 한번에 한 유저 신고
    - 횟수 제한 ㄴ
    - 중복 신고 가능, -> 신고 처리는 1회
    
    정지 
    - k번 이상 신고시 정지
    - 정지시 k명에게 메일 발송
    - 신고된 모든 내용을 취합하여 
    
    리턴
    - id_list 순으로, 신고 메일 받은 수 출력 
    
2. TC
    tc1)
        id  : ["a", "b", "c"]
        rp  : ["a b", "a c"]
        k   : 1
        res : [2,0,0]
        
    tc2)
        id  : ["a", "b"]
        rp  : ["a b", "b a"]
        k   : 2
        res : [0,0]
        
    tc3)
        id  : ["a", "b"]
        rp  : ["a b", "b a"]
        k   : 1
        res : [1,1]
    
    tc4) -> rp < k 인경우는 모두 0 임 
        id  : ["a", "b"]
        rp  : ["a b", "b a"]
        k   : 3
        res : [0,0]
        
    tc5)
        id  : ["a", "b"]
        rp  : ["a b", "a b", "a b", "a b"]
        k   : 1
        res : [1,0]
        
        
3. Brain Storming
    a) init
        for i in range(len(id_list)):
            answer.append(0)
    b) tc4
        if rp < k:
            return answer
    c) 
    
    tc1)
        id  : ["a", "b", "c"]
        rp  : ["a b", "a c"]
        k   : 1
        res : [2,0,0]


            
        
    1. 유저가 신고한 id 추출 -> user_report 
        user_report = []
        report_cnt = []
        
        for i in range(len(id_list)):
            user_report.append([])
            report_cnt.append(0)
            
        for rp in report:
            user, reported = rp.split()
            user_report[id_list.index(user)].append(reported)
            report_cnt[id_list.index(reported)] += 1
            
            
            
    2. 정지된 id 계산 -> blocked 
        blocked = []
        
        for user in id_list:
            if report_cnt[id_list.index(user)] >= k:
                blocked.append(user)
        
    
        
        
    3. user_report와 blocked의 교집합 원소 개수 구하기 
        for i in range(len(id_list)):
            for b in blocked:
                answer[i] += user_report[i].count(b)
                
                
                
4. Summarize

        user_report = []
        report_cnt = []
        
        for i in range(len(id_list)):
            user_report.append([])
            report_cnt.append(0)
            
        for rp in report:
            user, reported = rp.split()
            user_report[id_list.index(user)].append(reported)
            report_cnt[id_list.index(reported)] += 1
   
20:38
    
'''