def solution(info, query):
    answer = []
    input_list = []
    for i in info:
        input_list.append(i.split()) 
        # lang, part, pos, food, score 
    
        
    for i in range(len(query)):
        lang, part, pos, food = query[i].split(" and ")
        food, score = food.split()
    
        passed = input_list
        
        
        passed = filter(lambda x: int(x[4]) >= int(score), passed)
        # if lang != "-":
        
        passed = filter(lambda x: x[0] == lang and x[1] == part and x[2] == pos and x[3] == food, passed)
#         if part != "-":
#             passed = filter(lambda x: x[1] == part, passed)
#         if pos != "-":
#             passed = filter(lambda x: x[2] == pos, passed)
#         if food != "-":
#             passed = filter(lambda x: x[3] == food, passed)    
            
        
        
        passed = list(passed)
        answer.append(len(passed))
    
    return answer


# def solution(info, query):
#     answer = []
#     input_list = []
#     query_list = []
    
#     for i in info:
#         input_list.append(i.split()) 
#         # lang, part, pos, food, score 
#     for q in query:
#         # query_list.append(q.split()) 
#         lang, part, pos, food = q.split(" and ")
#         food, score = food.split()
#         query_list.append([lang, part, pos, food, score])
#         # passed = input_list
#         # lang, part, pos, food, score 
    
    
#     for i in range(len(query)):
#         now_q = query_list[i]
#         count = 0
#         for j in range(len(input_list)):
#             now_info = input_list[j]
        
#             if int(now_info[4]) >= int(now_q[4]):
#                 if now_q[0] == "-" or now_info[0] == now_q[0]:    
#                     if now_q[1] == "-" or now_info[1] == now_q[1]:    
#                         if now_q[2] == "-" or now_info[2] == now_q[2]:    
#                             if now_q[3] == "-" or now_info[3] == now_q[3]:    
#                                 count += 1
    
#         answer.append(count)
    
#     return answer

'''
18:10




17:40 - 18:09 
1. Problem is...?
    - lang
    - part
    - position
    - food
    - score
    - return user.count
    
3. Barin Storming
    - input -> input_list
    
    input_list = []
    query_list = []
    for i in info:
        input_list.append(i.split()) 
        # lang, part, pos, food, score 
    
    for q in query:
        query_list.append(q.split()) 
        # lang, part, pos, food, score 
        
       
    for i in range(len(query)):
        lang, part, pos, food = query[i].split(" and ")
        food, score = food.split()
        passed = input_list
        
        if lang != "-":
            passed = filter(lambda x: x[0] == lang, passed)
        if part != "-":
            passed = filter(lambda x: x[1] == part, passed)
        if pos != "-":
            passed = filter(lambda x: x[2] == pos, passed)
        if food != "-":
            passed = filter(lambda x: x[3] == food, passed)
        if score != "-":
            passed = filter(lambda x: x[4] >= score, passed)
        
        
        answer.append(len(passed))
    
4.
def solution(info, query):
    answer = []
    input_list = []
    for i in info:
        input_list.append(i.split()) 
        # lang, part, pos, food, score 
    
        
    for i in range(len(query)):
        lang, part, pos, food = query[i].split(" and ")
        food, score = food.split()
        passed = input_list
        
        if lang != "-":
            passed = filter(lambda x: x[0] == lang, passed)
        if part != "-":
            passed = filter(lambda x: x[1] == part, passed)
        if pos != "-":
            passed = filter(lambda x: x[2] == pos, passed)
        if food != "-":
            passed = filter(lambda x: x[3] == food, passed)    
            
        passed = filter(lambda x: int(x[4]) >= int(score), passed)
        
        passed = list(passed)
        answer.append(len(passed))
    
    return answer
    
'''