'''
Bubble sort는 가장 작은 수를 맨 마지막으로 보내는(내림차순의 경우) 로직입니다. 
하지만 이 문제에서 '사전순으로 가장 뒤서는 것'이란 앞쪽에 가장 큰 수들을 위치시키는 것이 우선입니다. 
따라서 s 교환 내에서 가장 큰 수를 앞쪽으로 많이 보내는 방법을 구현해야 합니다.
'''

import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
s = int(sys.stdin.readline())

start = 0
breaker = False
while start < n :
    maxval = max(a[start:start+s+1])
    maxidx = a.index(maxval)
    # print(f'{maxval=}:{maxidx=}:{start=}')

    for i in range(maxidx,start,-1) :
        if a[i-1] < a[i] :
            a[i-1], a[i] = a[i], a[i-1]
            s -= 1
        # print(f'{s=}:{a=}')
        if  s==0 : 
            breaker = True
            break
    if breaker : break
    start += 1
print(*a)
