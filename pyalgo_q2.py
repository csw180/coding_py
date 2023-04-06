import re
def solution(data):
    answer = 0
    result = re.findall('[rev][0-9]+',data)
    for r in result :
        num = int(r[1:]) if 1 <= int(r[1:]) <=10 else int(r[1])
        answer += num
    return f'{answer//10}월 {answer%10:2d}일'

print(solution('a10b9r1ce33uab8wc918v2cv11v9'))