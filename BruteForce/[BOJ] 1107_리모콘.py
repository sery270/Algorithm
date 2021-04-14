N = int(input())
N_str = str(N)
M = int(input())
broken = []
if M > 0:
  broken = list(map(int, input().split()))
now = 100
sol = 10000000


def possible(a):
    if a in broken:
      # print(a)
      return False
    return True


# 숫자 안누르고, +,- 버튼을 누르는 경우
sol = min(abs(now - N), sol)

# 숫자를 누르고 +,- 버튼을 누르는 경우
# +만 누르는 경우

pos = True

# range(0,10)이면, 0,1,2,3,4,5,6,7,8,9 이다 !! 
for now_plus in range(N + 1, 1000001, 1):
    now_plus_str = str(now_plus)
    for i in range(0, len(now_plus_str)):
        if possible(int(now_plus_str[i])) == False:
            pos = False
            break
    # 모든 숫자가 가능할 때
    if pos:
        # 여기서 len(now_plus_str) 대신에 len(N_str)을 넣어서 틀렸다..
        sol = min(abs(N - now_plus)+len(now_plus_str), sol)
        # print(now_plus)
        break
    pos = True

# -만 누르는 경우
# 숫자만 누르는 경우 (N부터 시작)
pos = True

for now_plus in range(N, -1, -1):
    now_plus_str = str(now_plus)
    for i in range(0, len(now_plus_str)):
        if possible(int(now_plus_str[i])) == False:
            pos = False
            break
    # 모든 숫자가 가능할 때
    if pos:
        sol = min(abs(N - now_plus)+len(now_plus_str), sol)
        # print(now_plus)
        break
    pos = True

print(sol)
