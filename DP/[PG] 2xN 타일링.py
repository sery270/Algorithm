def solution(n):
    answer = 0
    mem = [ 0 for _ in range(n+1) ]
    mem[0] = 1 
    mem[1] = 1
    for i in range(2, n+1):
        mem[i] = (mem[i-1] + mem[i-2]) % 1000000007
    answer = mem[n]
    return answer