
# https://www.acmicpc.net/problem/1074
# Z 

import sys

def explore(start,n,r,c) :
    if n==1 :  return start + (2*r+c)

    w, hw = 2**n, (2**n)//2
    result = 0
    if (r < hw)  and (c < hw) :  #2사분면
        result = explore(start,n-1,r,c)
    elif (r < hw)  and (c >= hw) :  #1사분면
        result = explore(start+(hw**2),n-1,r,c-hw)
    elif (r >= hw)  and (c < hw) :  #3사분면
        result = explore(start+(w*hw),n-1,r-hw,c)
    else :  #4사분면
        result = explore(start+(hw**2)+(w*hw),n-1,r-hw,c-hw)
    return result
        

N,r,c = map(int,sys.stdin.readline().split(' '))
print(explore(0,N,r,c))

