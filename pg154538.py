from collections import deque

def solution(x, y, n):
    cnt = 0
    dq = deque()
    dq.append((cnt,y))
    while dq :
        cnt,v = dq.popleft()
        if v==x :
            return cnt
        cnt +=1
        if v-n > 0 :
            dq.append((cnt,v-n))
        if v%2==0 :
            dq.append((cnt,v//2))
        if v%3==0 :
            dq.append((cnt,v//3))    
    return -1


print(solution(10,40,5))
print(solution(10,40,30))
print(solution(20,20,4))
print(solution(2,5,4))