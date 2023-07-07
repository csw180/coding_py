# 프로그래머스 최소값만들기:12941 https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(a,b) :
    a.sort()
    b.sort(reverse=True)
    return sum([x*y for x,y in zip(a,b)])

print(solution([1, 4, 2],[5, 4, 4]))
print(solution([1,2],[3,4]))