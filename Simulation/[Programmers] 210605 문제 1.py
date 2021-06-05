def solution(s):
    answer = []

    s_prev = ""

    ix_prev = -1

    tmp = ""

    if len(s) >=2 :
        if s[0] == s[1]:
            answer = [""]


    for i in range(len(s)):

        if s[i] == s_prev:
            print(answer)
            if tmp[:-1] != '':
                answer.append(tmp[:-1])
                tmp = ''

            ix_prev = i
            continue
        else:
            # print(answer)
            s_prev = s[i]
            tmp = s[ix_prev+1:i+1]

    print(answer)

    # if answer[-1] != "" and s[ix_prev+1:i+1] != "":
        # answer.append(s[ix_prev+1:i+1])
    answer.append(s[ix_prev+1:i+1])


    # if s[ix_prev+1:i+1] != "":
    #     answer.append(s[ix_prev+1:i+1])





    t = True
    for s in answer:
        if s == "":
            continue
        else:
            t = False
            break  
    if t:
        answer = ["",""]

#     if answer == ["","",""]:


#     if len(answer) >= 1:
#         answer.append("")



    return answer