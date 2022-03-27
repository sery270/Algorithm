import re
def solution(logs):
    answer = 0 
    log_name = ["team_name : ","application_name : ","error_level : ","message : "]

    for log in logs:
        if len(log) > 100: # 로그의 길이는 100 이하여야 합니다.
            answer += 1
            continue
        else:
            invalid = False

            # 앞뒤 공백 확인 (불필요한 공백 확인)
            # 연속된 공백 확인 
            blank = log.split()
            cmpare = " ".join(blank)

            if log != cmpare:
                answer += 1
                continue

            # 누락 된 정보 있는지 확인 && 정보 이름이 정확한지 
            for name in log_name:
                if log.count(name) == 0:
                    answer += 1
                    invalid = True
                    break
            if invalid:
                continue
            


            # data cleaning
            for name in log_name:
                log = log.replace(name, '')
            log = log.split() # [db, dbtest info test]

            # 내용이 다 있는지 == 길이 1 이상인지
            if len(log) != 4:
                answer += 1
                continue

            # 알파벳 소문자 혹은 알파벳 대문자만 있는지 확인
            for l in log:
                cmpare = re.sub('[^a-zA-Z]','', l) 
                if l != cmpare:
                    answer +=1
                    invalid = True
                    break
            if invalid:
                continue
    return answer



'''
1. Problem is...? 
    - 알파벳 소문자 혹은 알파벳 대문자

2. TC

tc1)
"team_name : db 
application_name : dbtest 
error_level : info 
message : test", 

tc2)
"team_name : test 
application_name : I DONT CARE 
error_level : error 
message : x", 

tc3)
"team_name : ThisIsJustForTest 
application_name : TestAndTestAndTestAndTest 
error_level : test 
message : IAlwaysTestingAndIWillTestForever", 

tc4)
"team_name : oberervability 
application_name : LogViewer 
error_level : error"

tc5)
"team_name : db 
application_name : dbtest 
error_level : info 
message : ", 

tc6)
"team_name : db 
application_name : dbtest 
error_level : in:fo", 

tc7)
"team_name : db 
application_name : dbtest 
error_level : info 
message :         test", 
3. Brain Storming

"team_name : db 
application_name : dbtest 
error_level : info 
message : test", 

    - split(" : ") => 위험함, 
    - 누락 된 정보 있는지 확인 && 정보 이름이 정확한지 
        ":" 의 개수 카운트
            - ":" 4개 이상 => 특수 문자가 있다는 이야기이므로 수집 ㄴ
            - ":" 4개 이하 => 누락 되었다 수집 ㄴ 
            - ":" 4개  => 누락 되었다 수집 ㄴ 

        log_name = ["team_name : ","application_name : ","error_level : ","message : "]

        for name in log_name:
            if log.count(name) == 0:
                # 수집하지 않는 로그 


    - 알파벳 소문자 혹은 알파벳 대문자만 있는지 확인
        - 공백 ㄴ
        - 숫자 ㄴ
        - 특수문자 ㄴ
        
        for name in log_name:
            log = log.replace(name, '')
        # db dbtest info test
        log = log.split()
        # [db dbtest info test]

        nowlog # db
        cmp = re.sub('[^a-zA-Z]','', nowlog) # 알파벳 소문자 혹은 알파벳 대문자가 아닌 것 제거
        if cmp != nowlog;
            # 수집하지 않는 로그 


    - 로그 길이 
        if len(log) > 100:
            # 수집하지 않는 로그 

4. Summarize
    answer = 0 
    log_name = ["team_name : ","application_name : ","error_level : ","message : "]

    for log in logs:
        if len(log) > 100: # 로그의 길이는 100 이하여야 합니다.
            answer += 1
            contiue
        else:
            invalid = False

            # 앞뒤 공백 확인 (불필요한 공백 확인)
            # 연속된 공백 확인 
            blank = log.split()
            cmp = " ".join(blank)

            if log != cmp:
                answer += 1
                continue

            # 누락 된 정보 있는지 확인 && 정보 이름이 정확한지 
            for name in log_name:
                if log.count(name) == 0:
                    answer += 1
                    invalid = True
                    break
            if invalid:
                continue
            


            # data cleaning
             
            
            for name in log_name:
                log = log.replace(name, '')
            log = log.split() # [db, dbtest info test]

            # 내용이 다 있는지 == 길이 1 이상인지
            if len(log) != 4:
                answer += 1
                continue

            # 알파벳 소문자 혹은 알파벳 대문자만 있는지 확인
            for l in log:
                
                cmp = re.sub('[^a-zA-Z]','', l) 
                if l != cmp:
                    answer +=1
                    continue

            


        for name in log_name:
            log = log.replace(name, '')
        # db dbtest info test
        log = log.split()
        # [db dbtest info test]

        nowlog # db
        cmp = re.sub('[^a-zA-Z]','', nowlog) # 알파벳 소문자 혹은 알파벳 대문자가 아닌 것 제거
        if cmp != nowlog;
            # 수집하지 않는 로그 



'''