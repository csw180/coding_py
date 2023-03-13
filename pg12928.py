from math import sqrt

def divisor(n) :
    result = []
    for i in range(1,int(sqrt(n))+1) :
        if n%i==0 :
            result.append(i)
            if i!=(n//i) : result.append(n//i)
    return result

        
def solution(n):
    ds = divisor(n)
    return sum(ds)

print(solution(12))
print(solution(5))