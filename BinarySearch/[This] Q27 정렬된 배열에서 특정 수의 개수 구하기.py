# 18:56
N, x = map(int, input().split())
numlist = list(map(int, input().split()))

start, end = 0, N-1
now = (start+end)//2
answer = -1 

while start < end:
  now = (start+end)//2
  if numlist[now] == x:
    if numlist[start] < x:
        start = start+1
    if numlist[end] > x:
        end = end-1
    if numlist[start] == numlist[end]:
        answer = end - start + 1
        break
  if numlist[now] < x:
    start = now
    continue
  if numlist[now] > x:
    end = now
    continue

print(answer) 

# 19:25

'''
1. Problem is...?
  x의 개수를 찾는 것 

2. TC 
tc1)
4 1
1 1 1 2
res    : 3

tc2)
3 1
2 2 2
res    : -1

tc3)
4 -1
-10 -1 0 0
res    : 1

3. Brain Storming
    a) binary search
        - sorted data

if numlist[now] == x:
  
if numlist[now] < x:
  start = now
if numlist[now] > x:
  end = now

    b) x의 위치
        - start -> now.val == x && now.left < x
        - end -> now.val == x && now.right > x  

        xstartpos = -1
        xendpos = -1

        if numlist[now] == x:
          if numlist[now-1] < x:
              xstartpos = now-1
          if numlist[now+1] > x:
              xendpos = now+1
          
    c) x의 개수
        - end pos - start pos 


4. Summarize


4 1

      s m       e
0 0 0 1 1 1 1 1 1 2
0 1 2 3 4 5 6 7 8 9
8-3 = 5

3 1
s n e
2 2 2



start, end = 0, N-1
now = (start+end)//2
answer = -1 

while start < end:
  now = (start+end)//2
  if numlist[now] == x:
    if numlist[start] < x:
        start = start+1
    if numlist[end] > x:
        end = end-1
    if numlist[start] == numlist[end]:
        answer = end - start + 1
        break
  if numlist[now] < x:
    start = now
    continue
  if numlist[now] > x:
    end = now
    continue



return answer

    

      




'''
