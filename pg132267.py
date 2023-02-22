def solution(a, b, n):
    answer = 0
    while (n>=a) :
        m,r = divmod(n,a)
        answer += m*b
        n = m*b+r
    return answer

print(solution(2,1,20))
print(solution(3,1,20))