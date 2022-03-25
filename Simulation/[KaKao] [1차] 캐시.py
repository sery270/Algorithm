from collections import deque

def solution(cacheSize, cities):
    answer = 0
    dq = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in dq: # hit
            dq.remove(city)
            dq.append(city)
            answer += 1 
        else: # miss
            dq.append(city)
            answer += 5
    return answer


'''
1. PRoblem is...?
    - LRU
    
2.

3. Brain Storming
    - deque
    - maxsize


'''