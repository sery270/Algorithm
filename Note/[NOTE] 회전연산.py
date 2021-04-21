from collections import deque

N = int(input()) # input : 12
print(N)
print(type(N))
# 12
# <class 'int'>

N_str = str(N)
print(N_str)
print(type(N_str))
# 12
# <class 'str'>

N_str = N_str.zfill(4)
print(N_str)
print(type(N_str))
# 0012
# <class 'str'>

N_dq = deque(N_str)
print(N_dq)
print(type(N_dq))
# deque(['0', '0', '1', '2'])
# <class 'collections.deque'>

N_dq.rotate(1)
print(N_dq)
print(type(N_dq))
# deque(['2', '0', '0', '1'])
# <class 'collections.deque'>

# iterable의 join 연산
# iterable : list, dict, set, str, bytes, tuple, range

# dq의 내용물이 int, join 에서 에러나므로, str로 map을 해줘야함 
# N_list = list(map(str, N_dq))
# print(N_list)
# print(type(N_list))
# dq_str = "".join(dq_list)

# dq의 내용물이 str,바로 dq를 넣어도 결과는 같음
N_str = "".join(N_dq)
print(N_str)
print(type(N_str))
# 2001
# <class 'str'>

N = int(N_str)
print(N)
print(type(N))
# 2001
# <class 'int'>