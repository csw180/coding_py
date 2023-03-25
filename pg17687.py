# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def to_base_n(n,base) :
    board = '0123456789ABCDEF'
    if n==0 : return '0'
    result = ''
    while n :
        result = board[n % base] + result
        n //= base
    return result
        
def solution(n, t, m, p):
    answer = ''
    start = 0
    merged_str =''
    while len(merged_str) <= t*m :
        merged_str += to_base_n(start,n)
        start +=1
    for i in range(p-1,t*m,m) :
        answer += merged_str[i]
    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))