from collections import deque

def solution(begin, target, words):
    words.sort()
    if target in words:
        before = ["" for _ in range(len(words))]
        queue = deque([begin])
        while queue:
            now = queue.popleft()
            for j in range(0, len(words)):
                word = words[j]
                for i in range(0, len(now)):
                    # now_tmp = now.replace(now[i],"")
                    # word_tmp = word.replace(word[i],"")
                    now_tmp = now[:i] + now[i+1:]
                    word_tmp = word[:i] + word[i+1:]
                    # print(now_tmp)
                    # print(word_tmp)
                    if now_tmp == word_tmp and before[j] == "":
                        queue.append(word)
                        before[j] = now
                        # print("appended!")

        now = target
        cnt = 0
        while True:
            if words.index(now) or words.index(now) == 0:
                now = before[words.index(now)]
                if now == '':
                    cnt = 0
                    break
                if now == begin:
                    cnt += 1
                    break
                cnt += 1
            else:
                cnt += 1
                break
        answer = cnt
    else:
        answer = 0

    # print(answer)
    return answer

solution("hit",	"cog",	["cog", "log", "lot", "dog", "dot", "hot"])
solution("hit",	"cog",	["cog", "lot", "dog", "dot", "log", "hot"])
solution("aaa",	"acb",	["abb", "aas", "aca", "acb", "acc","aac"])