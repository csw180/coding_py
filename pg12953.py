def  gcd(a,b) :  # 최대공약수 유클리드호제법
    if  a%b == 0 :
        return b
    else :
        return gcd(b,a%b)

def lcm(a,b) :
    return a*b // gcd(a,b)

def solution(arr):
    pre_lcm = arr[0]
    for i in range(1,len(arr)) :
        pre_lcm = lcm(pre_lcm,arr[i])
    return pre_lcm

print(solution([2,6,8,14]))
print(solution([1,2,3]))