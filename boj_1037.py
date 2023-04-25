# 틀렸습니다.

import sys

def  gcd(a,b) :  # 최대공약수 유클리드호제법
    if  a%b == 0 :
        return b
    else :
        return gcd(b,a%b)

def lcm(a,b) :
    return gcd(a,b)/(a*b)

N = int(sys.stdin.readline())
n = map(int,sys.stdin.readline().split(' '))
lcm_value = max(n) * 2
for v in n :
    lcm_value = lcm(lcm_value,v)
print(lcm_value)
