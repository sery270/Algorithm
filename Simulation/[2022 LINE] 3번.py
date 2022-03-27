def solution(num_teams, remote_tasks, office_tasks, employees):
    answer = []
    management = []
    for index, employee in enumerate(employees):
        ep = employee.split()

        team = int(ep[0])
        tasks = ep[1:]
        work = "remote"

        for task in tasks:
            if task in office_tasks:
                work = "office"
                break
        management.append([index+1, team, work])  
        
    # remote and office 구분하기 - type
    remote = []
    office = []

    office_team = [0] * (num_teams+1)

    for ep in management:
        if ep[2] == "office":
            office.append(ep)
            office_team[ep[1]] += 1
        else:
            remote.append(ep)


    # type == office가 0인 팀 찾기 
    need_change = []
    for i, team in enumerate(office_team):
        if team == 0:
            need_change.append(i) # 0도 들어감 !! 

    # 사원번호 빠른 사람의 type 변경
    for i, m in enumerate(management):
        if m[1] in need_change:
            management[i][2] = "office"
            need_change.remove(m[1])
        
    
    remote_ep = filter(lambda x: x[2] == "remote", management)

    for r in remote_ep:
        answer.append(r[0])
    answer = sorted(answer)
    return answer



'''
1. Problem is..?
    - filtering + @
    - 각팀에 한 명은 출근/ 팀 10개 이하
    - 사원 한 명은, 팀 번호(input) + 사원 번호(1,,,,len)
    
    - 재택근무 사원 구하기 ! 

2. tc
    tc1)
    모두가 재택
        num_teams,      3
        remote_tasks,   a
        office_tasks,   b
        employees       [1 a, 2 a, 3 a]
    tc2)
    모두가 출근
        num_teams,      1
        remote_tasks,   a
        office_tasks,   b
        employees       [1 a, 1 a, 1 a]
    tc3)
    모두 재택인데 출근해야함 
        num_teams,      1
        remote_tasks,   a
        office_tasks,   b
        employees       [1 a, 1 a, 1 a]
    
    tc4)
        num_teams,      1
        remote_tasks,   a
        office_tasks,   b
        employees       [1 a, 1 b, 1 a b]

    
3. Brainn Storming
    - 사원번호 부여하기 
        management =(ix, team, type)
        management 
        [
            {
                "id" : 1,
                "team" : 1,
                "type" : "",
            },
            {
                "id" : 2,
                "team" : 1,
                "type" : "",
            }
        ]
        =============
        [
            [1,1,"remote"], # [ix,team,"work type"]
            [2,1,"office"]
        ]

        for ep in employees:


    for index, employee in enumerate(employees):
        ep = employee.split()

        team = ep[0]
        tasks = ep[1:]
        type = "remote"

        for task in tasks:
            if task in office_tasks:
                type = "office"
                break
        

        management.append([index+1, team, type])  


        
    - remote and office 구분하기 - type
        remote = []
        office = []

        office_team = [0] * (len(employees)+1)

        for ep in management:
            if ep[2] == "office":
                office.append(ep)
                office_team[ep[1]] += 1
            else:
                remote.append(ep)


    - type == office가 0인 팀 찾기 
        need_change = []
        for i, team in enumerate(office_team):
            if team == 0:
                need_change.append(i)

    - 사원번호 빠른 사람의 type 변경
            for i, m in enumerate(management):
                if m[1] in need_change:
                    management[i][2] = "office"
                    need_change.remove(m[1])
        
    
    - return 
        management에 필터
        1. remote인 사람
        remote_ep = filter(lambda x: x[2] == "remote", management)
        2. 들의 ix 만 리스트로 리턴 
        for r in remote_ep:
            answer.append(r[0])

4. Summarize

    # 데이터 처리 [ix,team,"work type"]
        # [
        #     [1,1,"remote"], 
        #     [2,1,"office"]
        # ]
   for index, employee in enumerate(employees):
        ep = employee.split()

        team = ep[0]
        tasks = ep[1:]
        type = "remote"

        for task in tasks:
            if task in office_tasks:
                type = "office"
                break
        

        management.append([index+1, team, type])  
        
    # remote and office 구분하기 - type
    remote = []
    office = []

    office_team = [0] * (len(employees)+1)

    for ep in management:
        if ep[2] == "office":
            office.append(ep)
            office_team[ep[1]] += 1
        else:
            remote.append(ep)


    # type == office가 0인 팀 찾기 
    need_change = []
    for i, team in enumerate(office_team):
        if team == 0:
            need_change.append(i)

    # 사원번호 빠른 사람의 type 변경
    for i, m in enumerate(management):
        if m[1] in need_change:
            management[i][2] = "office"
            need_change.remove(m[1])
        
    
    remote_ep = filter(lambda x: x[2] == "remote", management)

    for r in remote_ep:
        answer.append(r[0])



'''