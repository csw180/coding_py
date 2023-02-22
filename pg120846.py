def is_composit_number(n) :
    sqrt_value = n**(1/2)
    for i  in range(2,int(sqrt_value)+1)  :
        if n%i==0 :
            return True
    return False

def solution(n):
    result = []
    for i in range(1,n+1) :
        if is_composit_number(i) :
            result.append(i)
    # print(result)
    return len(result)

print(solution(10))
print(solution(15))

