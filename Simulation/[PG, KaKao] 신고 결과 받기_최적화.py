def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dic = {user:0 for user in id_list}
    
    
    for rp in set(report):
        reporter, reported = rp.split()
        report_dic[reported] += 1
        
    for rp in set(report):
        reporter, reported = rp.split()
        if report_dic[reported] >= k: # True 면 정지된 유저 
            answer[id_list.index(reporter)] += 1
        
    
    return answer



'''
ans     : [1,0,0]
r_dic   : {a:0, b:1, c:0}

    tc3)
        id  : [a,b,c]
        rp  : ["a b", "a b"]
        k   : 1
        res : [1,0,0]




1. Problem is...?
    신고
    - 한번에 한명
    - 중복 신고 가능, 처리는 1번
    정지
    - k명에게 신고당하면 정지 
    
    메일
    - 정지 당하면, 신고한 k 명에게 메일 발송
    
2. TC
    tc1)
        id  : [a,b,c]
        rp  : ["a b", "a c"]
        k   : 1
        res : [2,0,0]
        
    tc2)
        id  : [a,b,c]
        rp  : ["a b", "a c"]
        k   : 2
        res : [0,0,0]

    tc3)
        id  : [a,b,c]
        rp  : ["a b", "a b"]
        k   : 1
        res : [1,0,0]

    tc3) len(rp) < k 는 항상 0임 
        id  : [a,b,c]
        rp  : ["a b", "a b"]
        k   : 3
        res : [0,0,0]
        
3. Brain Storming
    tc1)
        id  : [a,b,c]
        rp  : ["a b", "a c"]
        k   : 1
        res : [2,0,0]
        
    0. 초기 세팅
        answer  : [0,0,0] 
        reported : [a:0, b:0, c:0]
        
        answer = [0] * len(id_list)
        report_dic = {x:0 for x in id_list}
        
        
    1. 중복 신고 제거 => set
    2. 각 유저 신고 횟수 카운트 (정지 여부를 판단하기 위해)
    
        for rp in set(report):
            user, reported = rp.split()
            report_dic[reported] += 1

    3. 정지 유저 판별 
    4. user가 신고한 blocked 카운트 (answer에 기록)
        for rp in set(report):
            user, blocked = rp.split()
            if report_dic[blocked] > k:
                answer[id_list.index(user)] += 1
                
4. Summarize

        answer = [0] * len(id_list)
        report_dic = {x:0 for x in id_list}
    
        for rp in set(report):
            user, reported = rp.split()
            report_dic[reported] += 1    
    
        for rp in set(report):
            user, blocked = rp.split()
            if report_dic[blocked] > k:
                answer[id_list.index(user)] += 1        
    
    
    

'''