def solution(n):
    last = n//2 if n%2==0 else n//2+1
    return [1+(2*i) for i in range(last)]


print(solution(10))
print(solution(11))
print(solution(15))