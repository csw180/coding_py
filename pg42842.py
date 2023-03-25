# r : 노란색 격자의 행의 수
# c : 노란색 격자의 열의 수
def solution(brown, yellow):
    answer = []
    maxvalue = brown if brown > yellow else yellow
    for r in range(1,maxvalue) :
        if  yellow % r != 0 : continue
        c = yellow // r
        if  (r+c == (brown/2) -2) :
            answer.append(r+2)
            answer.append(c+2)
            break
    return sorted(answer,reverse=True)

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))