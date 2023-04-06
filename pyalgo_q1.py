def solution(data):
    answer = ''
    for d in data :
        d = d.replace(' ','')
        bin = ''.join(['1' if s=='+' else '0' for s in d])
        answer += chr(int(bin,2))
    return answer

print(solution([' + - - + - + - ', ' + + + - + - + ', ' + + - + + + - ']))
print(solution([' + + + - - + + ', ' + + + - + - - ', '++----+', '+++ --+ -', '+++-+ - -']))
print(solution([' + + - - - - + ', ' + + - + + - - ', '+ +-- +++ ', ' ++- ++++']))