#     # P를 대상으로 맨해튼 거리 계산
#     # O는 의미 없음
#     # X는 의미 있음 
#     # mh_dis == 0 인 경우 -> 없음
#     # mh_dis == 1 인 경우 -> 인접해서 앉음, r이나 c 둘 중 하나가 같고, 인접함
#     # mh_dis == 2 인 경우 -> 대각선으로 앉음/ r이나 c 둘 중 하나가 같고, 한 칸 띄워서 앉음

#     # 따라서, 안되는 경우는 아래 6가지임

#     # PP P
#     #    P

#     # PO OP POP P
#     # OP PO     O
#     #           P

#     # PP P
#     #    P

#     # PO OP PO OP PX XP POP P
#     # OP PO XP PX OP PO     O
#     #                       P
def solution(places):
    answer = []

    for room in range(0,5):
        for row in range(0,5):
            if 'PP' in places[room][row]:
                answer.append(0)
                break
            if 'POP' in places[room][row]:
                answer.append(0)
                break
            if 'PO' in places[room][row]:
                indices = list(filter(lambda x: places[room][row][x:x+2] == 'PO', range(len(places[room][row]))))
                # print(indices)
                b = False
                if row+1<5:
                    for index in indices:
                        if places[room][row+1][index:index+2] == 'OP':
                            answer.append(0)
                            b = True
                            break
                        if places[room][row+1][index:index+2] == 'XP':
                            answer.append(0)
                            b = True
                            break
                if b :
                    break
            if 'OP' in places[room][row]:
                indices = list(filter(lambda x: places[room][row][x:x+2] == 'OP', range(len(places[room][row]))))
                b = False
                if row+1<5:
                    for index in indices:
                        if places[room][row+1][index:index+2] == 'PO':
                            answer.append(0)
                            b = True
                            break
                        if places[room][row+1][index:index+2] == 'PX':
                            answer.append(0)
                            b = True
                            break
                if b:
                    break
            if 'XP' in places[room][row]:
                indices = list(filter(lambda x: places[room][row][x:x+2] == 'XP', range(len(places[room][row]))))
                b = False
                if row+1<5:
                    for index in indices:
                        if places[room][row+1][index:index+2] == 'PO':
                            answer.append(0)
                            b = True
                            break
                if b:
                    break
            if 'PX' in places[room][row]:
                indices = list(filter(lambda x: places[room][row][x:x+2] == 'PX', range(len(places[room][row]))))
                b = False
                if row+1<5:
                    for index in indices:
                        if places[room][row+1][index:index+2] == 'OP':
                            answer.append(0)
                            b = True
                            break
                if b:
                    break
                
            if 'P' in places[room][row]:
                indices = list(filter(lambda x: places[room][row][x:x+1] == 'P', range(len(places[room][row]))))
                b = False
                if row+1<5:
                    for index in indices:
                        if places[room][row+1][index:index+1] == 'P':
                            answer.append(0)
                            b = True
                            break
                        elif places[room][row+1][index:index+1] == 'O':
                            if row+2<5:
                                if places[room][row+2][index:index+1] == 'P':
                                    answer.append(0)
                                    b = True
                                    break
                if b:
                    break
        else:
            answer.append(1)

    return answer