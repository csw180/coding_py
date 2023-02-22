from functools import reduce

def GCD(a,b) :
    """
    유클리드 호제법을 이용해 최대공약수를 가져온다.
    """
    s,b = min(a,b), max(a,b)
    while(b % s) :
        b, s = s,b % s
    return s

def get_devisors(n) :
    """
    최대공약수의 약수들이 두수의 공약수들 이다
    약수를 구하기 위하여 n 까지 반복 필요없고
    루트n 까지만 나눠보고 나눠지는 제수와 피제수를 다 모으면 된다
    """
    sqrt_value = n**(1/2)
    result = []
    for i  in range(1,int(sqrt_value)+1)  :
        if n%i==0 :
            result.append(i)
            if i!=(n//i) : result.append(n//i)
    return result

def solution(arrayA, arrayB):
    divs = get_devisors(reduce(GCD,arrayA))
    filtered = []
    for v in divs:
        if v!=1 and len(list(filter(lambda x : x%v==0,arrayB))) == 0 :
            filtered.append(v)
    case1 = max(filtered) if len(filtered) > 0 else 0

    divs = get_devisors(reduce(GCD,arrayB))
    filtered = []
    for v in divs:
        if v!=1 and len(list(filter(lambda x : x%v==0,arrayA))) == 0 :
            filtered.append(v)
    case2 = max(filtered) if len(filtered) > 0 else 0

    return max(case1, case2)

print(solution([10, 17],[5, 20]))
print(solution([10, 20],[5, 17]))
print(solution([14, 35,119],[18,30,102]))
