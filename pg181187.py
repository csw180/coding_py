import math
def solution(r1, r2):
    answer = 0
    for x in range(r2,0,-1) :
        if  x >= r1 :
            answer += int(math.sqrt(r2**2 - x**2))+1
        else :
            answer += int(math.sqrt(r2**2 - x**2))+1 - math.ceil(math.sqrt(r1**2 - x**2))

    return answer * 4

print(solution(2,3))