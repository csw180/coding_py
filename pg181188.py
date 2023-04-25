def solution(targets):
    answer = 0
    targets.sort(key=lambda x : (x[0],x[1]))
    min_value = 100_000_000
    for target in targets :
        if  target[1] < min_value :
            min_value = target[1]
        elif target[0] >= min_value :
            answer += 1 
            min_value = target[1]
    return answer + 1

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))