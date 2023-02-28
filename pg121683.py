from collections import Counter

def solution(input_string):
    answer = ''
    zip_str = ''
    pre_str = ''
    for c in input_string :
        if  pre_str and pre_str == c :
            continue
        else :
            pre_str = c
            zip_str += c
    
    countor = Counter(zip_str)
    for k, v in sorted(countor.items()) :
        if  v > 1 :
            answer += k

    return answer if answer  else 'N'

print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))