import string
import itertools

# 문장 집합 만드는 함수
def getset(s):
    s = s.lower().replace(" ",'')
    return set(list(s))

# 점수 계산하는 함수 
def calScore(sentence, char_set):
    if sentence.islower(): # 대문자 없음 
        if char_set >= getset(sentence):
            return len(sentence)
        else:
            return 0
    else: # 대문자 있음
        if not "shift" in char_set:
            return 0
        else:
            upper_cnt = len(list(filter(lambda c:c in string.ascii_uppercase, sentence)))
            if char_set >= getset(sentence):
                return len(sentence) + upper_cnt
            else:
                return 0  

def solution(sentences, n):
    answer = 0
    # 등장 문자열 집합 
    char_set = []
    for s in sentences:
        s = s.lower().replace(" ",'')
        char_set += list(s)
    char_set = set(char_set)
    
    # shift 추가 
    for s in sentences:
        if not s.islower():
            char_set.add("shift")
            break

    # print(char_set)
    # print(calScore("LINE", char_set))
    if len(char_set) <= n:
        totalScore = 0
        for s in sentences:
            totalScore += calScore(s, char_set)
        return totalScore
    else:
        # 모든 부분 집합
				# permutations ->> combination
        nPr = itertools.permutations(list(char_set), n)
        
        for cb in nPr:
            cb = set(cb)     
            # 현재 조합으로 점수 계산 
            totalScore = 0
            for s in sentences:
                totalScore += calScore(s, cb)
            # max
            if totalScore > answer:
                answer = totalScore
    return answer


'''
1. Problem is,.,?
    - space + @
    - @ => shift, a-z 
    - 부분점수 ㄴ
    - 최대점수 리턴 

2. TC
    tc1)
        st      : ["line in line"]
        n       : 1
        res     : 0
    tc2)
        st      : ["l l l l"]
        n       : 1
        res     : 4
    tc3)
        st      : ["LLLLLL L L L"]
        n       : 2
        res     : 18

3. Brain Storming   
    - 문자 종류?
    - 뭔가 집합을 활용하면 좋을듯 ㅇㅇ 
    - 대문자 개수도 카운트 해야함 ㅜ
        - shift 포함 => N-1
        - shift 미포함 => N
    - 음 Counter ? 사용해봄직함 but, 문자 완성이 조건임 => ㄴㄴ 
    - 문자 종류가 > N 인건 제외 
    - 부분 집합으로 가야할듯 ? 

    - 각 문장의 소문자 집합을 구한다. 
    - 집합의 크기 <= N 인 합집합을 구한다. 


    - 제약
        15개 * 100000길이 = 150000 BF 가능...? 순열은 좀 무리 

    - 뭔가 카카오 양궁대회랑 비슷한데 
        - 조합문제임
        - 점수를 비교해서 리턴해야함 
        - dfs ?

    - 일단 대상 문자열 집합 생성 ! 
        # 등장 문자열 집합 
        char_set = []
        for s in sentences:
            s = s.lower().replace(" ",'')
            char_set += list(s)
        char_set = set(char_set)
        # print(char_set)

    - shift 여부 생각하기 
        if sentence.islower():
            # 대문자 없음 
        else:
            # 대문자 있음

    - 각 문장 집합 만들기 
        def getset(s):
            s = s.lower().replace(" ",'')
            return set(list(s))
    - 점수 계산 
        def calScore(sentence, char_set):
            if sentence.islower(): # 대문자 없음 
                if char_set > getset(sentence):
                    return len(sentence)
                else:
                    return 0
            else: # 대문자 있음
                if not "shift" in char_set:
                    return 0
                else:
                    upper_cnt = len(list(filter(lambda c:c in string.ascii_uppercase, sentence)))
                    if char_set > getset(sentence):
                        return len(sentence) + upper_cnt
                    else:
                        return 0




    - 이제 char_set 가지고 부분 집합으로 돌려봐야함 => n 순열 돌려서 점수 계산 and max ! 
        # 모든 부분 집합
        nPr = itertools.permutations(list(char_set), n)
        
        for cb i nPr:
            cb = set(cb)     
            # 현재 조합으로 점수 계산 
            totalScore = 0
            for s in sentences:
                totalScore += calScore(s, cb)
            # max
            if totalScore > max:
                max = totalScore


        부분 집합으로 돌리기 

        max 계산

'''