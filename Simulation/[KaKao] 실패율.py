def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)





'''

            from collections import Counter
            
            frate = []
            for i in range(1,N+1):
                frate.append((i,0))
            # frate = [(1,0),(2,0),(3,0),(4,0),(5,0)]    
                        
            left = 0 
            all = len(stages)
            stages = Counter(stages)
            for k,v in stages:
                frate.append((k, v/(all-left))
                left += v
            
            # sort
            sorted(frate, key=lambda frate: frate[0]) 
            sorted(frate, key=lambda frate: frate[1], reverse=True) 
19:02

1. Problem is...?
    - 실패율 구하는 문제
        - 스테이지 도달 && 미 클리어 플레이어 수
        - 스테이지에 도달한 플레이어 
    - 실패율 높은 순 정렬
        - 작은 번호 스테이지 순 정렬 -> - 실패율 높은 순 정렬
    - 클리어 유저가 0이면 -> 실패율 0
    - N == 5  => 1,2,3,4,5,6
        
2. TC
    tc1) 
        N       : 5
        st      : [2, 1, 2, 6, 2, 4, 3, 3]	
        
        res     : 34215
        
        1       1/8
        2       3/7
        3       2/4
        4       1/2
        5       0/1
        -
        6       1/1
        
    
    tc2) 
        N       : 1
        st      : [1]
        res     : 1
        
    tc3)    
        N       : 2
        st      : [1,2,3]
        res     : 21
        
        1 > 1/3
        2 > 1/2
        -
        3 > 1/1
        
        21

3. Brain storming
    - 실패율 계산
        N       : 5
        st      : [2, 1, 2, 6, 2, 4, 3, 3]	
        
        res     : 34215
        
        1       1/8
        2       3/7
        3       2/4
        4       1/2
        5       0/1
        -
        6       1/1
        
        - 1 ~ N 짜리 튜플 배열 
            frate = []
            for i in range(1,N+1):
                frate.append((i,0))
            # frate = [(1,0),(2,0),(3,0),(4,0),(5,0)]
            
        - 인풋은 1~N+1인데, N+1은 계산 대상이 아님
            from collections import Counter
            
            len(stages)
            left = 0 
            stages = Counter(stages)
            for k,v in stage:
                frate.append((k,v/len(stages)-left))
                left += v
4. Summarize
            from collections import Counter
            
            frate = []
            for i in range(1,N+1):
                frate.append((i,0))
            # frate = [(1,0),(2,0),(3,0),(4,0),(5,0)]    
                        
            left = 0 
            all = len(stages)
            stages = Counter(stages)
            for k,v in stages:
                frate.append((k, v/(all-left))
                left += v
            
            # sort
            sorted(frate, key=lambda frate: frate[0]) 
            sorted(frate, key=lambda frate: frate[1], reverse=True) 
            
            
        
        
        
        
        
        
    

'''