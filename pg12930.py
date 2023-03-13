def solution(s):
    answer = ''
    idx = -1
    for v in s :
        if v.isalpha() :
            idx += 1
        else :
            idx = -1

        if idx == -1 :
            answer += ' '
        elif idx%2 :
            answer += v.lower()
        else :
            answer += v.upper()

    return answer

print(solution("try hello world"));