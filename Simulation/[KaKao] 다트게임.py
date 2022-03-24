def solution(dartResult):
    answer = 0
    score = []
    i = -1
    for c in dartResult:
        if c.isnumeric():
            i += 1
            if c == "0" and  len(score) > 0 and score[i-1] == "1":
                score[i-1] = "10"
                i -= 1
            else:
                score.append(c)

        elif c == "S":
            score[i] = int(score[i])**1
        elif c == "D":
            score[i] = int(score[i])**2
        elif c == "T":
            score[i] = int(score[i])**3

        elif c == "*":
            if len(score) > 1:
                score[i] *= 2
                score[i-1] *= 2
            else:
                score[i] *= 2
        elif c == "#":
            score[i] *= -1


    return sum(score)




'''
11:05
1. Problem is...?
    - scoring dart game

2. TC 

3. Brain Storming

c
1S2D*3T
i       : 2
score   : [1**1*2, 2**2*2, 3**3]

    score = []
    i = -1
    for c in dartResult:
        if c.isnumeric():
            i += 1
            score.append(int(c))

        elif c == "S":
            score[i] = score[i]**1
        elif c == "D":
            score[i] = score[i]**2
        elif c == "T":
            score[i] = score[i]**3

        elif c == "*":
            if len(score) > 1:
                score[i] *= 2
                score[i-1] *= 2
            else:
                score[i] *= 2

        elif c == "#":
            score[i] *= -1




'''