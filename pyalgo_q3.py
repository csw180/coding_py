import math
def solution(data:list):
    answer = []
    count = (len(data) * 30) // 100
    data.sort(key=lambda x: x[1]+x[2]+x[3]+x[4], reverse=True)
    if  count > 0 :
        for i in range(count) :
            answer.append(data[i][0])
    return answer

param = [['A', 25, 25, 25, 25], ['B', 10, 12, 13, 11], ['C', 24, 22, 23, 21], ['D', 13, 22, 16, 14]]
print(solution(param))
print(solution([['A', 25, 24, 11, 12], ['B', 13, 22, 16, 14]]))
