
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    
    # 2
    for char in new_id :
        if char.isalnum() or char in '_-.':
            answer += char
    
    # 3
    while True:
        if ".." in answer:
            answer = answer.replace("..", ".")
        else:
            break
    
    # 5
    if len(answer) == 0: 
        answer = "a"
    else : # 4
        if answer[0] == '.':
            if len(answer) == 1 :
                answer = "a"
            else:
                answer = answer[1:]
        if answer[-1] == '.':
            if len(answer) == 1 :
                answer = "a"
            else:
                answer = answer[:-1]
    
    
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7 
    tmp = answer[-1]
    while len(answer) < 3:
        answer += tmp
    
    return answer

