def solution(sides):
    max_value = max(sides)
    sides.remove(max_value)
    return 1 if sides[0]+sides[1] > max_value else 2

print(solution([1, 2, 3]))
print(solution([3, 6, 2]))
print(solution([199, 72, 222]))