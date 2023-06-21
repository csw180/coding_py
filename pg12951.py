# 프로그래머스  jadencase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    prev_char =''
    for w in s:
        if w.isalpha():
            if not prev_char or prev_char == ' ':
                answer += w.upper()
            else :
                answer += w.lower()
        else :
            answer += w
        prev_char = w
    return answer


print(solution('3people unFollowed me'))
print(solution('   for   the last week'))