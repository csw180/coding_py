# 백준 효율적인해킹(1325) https://www.acmicpc.net/problem/1325
# list 대신 공간절약을 위하여 dict 를 이용하는 버젼으로 바꿔봄
# 역시 시간초과

import sys
from collections import deque

input  = sys.stdin.readline

def bfs(start,coms) :
    q = deque()
    q.append(start)
    count = 0
    visited = dict()
    while q :
        c = q.popleft()
        if  visited.get(c) :
            continue
        visited[c] = True
        count += 1
        if  not coms.get(c) :
            continue
        for next in coms[c] :
            if  not visited.get(next) : 
                q.append(next)
    return count-1       # 자기자신은 count 에서 제외 -1

n, m = map(int,input().split())
coms = dict()

for _ in range(m) :
    frm,to = map(int,input().split())
    if  not coms.get(to) :
        coms[to] = [frm]
    else :
        coms[to].append(frm)
# print(f'{coms=}')

results =[]
max_value = 0
for k in  coms.keys() :
    count = 0
    count = bfs(k,coms)
    # print(f'{k=} {count=}')
    if  count > max_value :
        max_value = count
        results = [str(k)]
    elif count == max_value :
        results.append(str(k))

print(' '.join(results))
