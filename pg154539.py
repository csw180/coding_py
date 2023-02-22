def solution(numbers):
    stack =  []
    result = []
    for i,v in enumerate(numbers) :
        while(stack and stack[-1][1]<v) :
            result.append((*stack.pop(),v))
        stack.append((i,v))
    for v in stack:
        result.append((*v,-1))
    return list(map(lambda x : x[2],sorted(result, key=lambda v : v[0])))


print(solution([9, 1, 5, 3, 6, 2]))
print(solution([2, 3, 3, 5]))

