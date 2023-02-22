def get_devisors(n) :
    """
    약수를 구하기 위하여 n 까지 반복 필요없고
    루트n 까지만 나눠보고 나눠지는 제수와 피제수를 다 모으면 된다
    """
    sqrt_value = n**(1/2)
    result = []
    for i  in range(1,int(sqrt_value)+1)  :
        if n%i==0 :
            result.append(i)
            result.append(n//i)
    return result

def solution(n):
    result = get_devisors(n-1)
    return  min(list(filter(lambda x:x>1,result)))

print(solution(10))
print(solution(12))