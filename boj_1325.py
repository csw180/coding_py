# 백준 효율적인해킹(1325) https://www.acmicpc.net/problem/1325
# 시간초과

import sys
from collections import deque

input  = sys.stdin.readline

def bfs(start,trusts,n) :
    q = deque()
    q.append(start)
    count = 0
    visited = [False for _ in range(n+1)]
    while q :
        c = q.popleft()
        if visited[c] :
            continue
        visited[c] = True
        count += 1
        for next in trusts[c] :
            if not visited[next] : 
                q.append(next)
    return count-1       # 자기자신은 count 에서 제외 -1

n, m = map(int,input().split())
coms = [[] for _ in range(n+1)]
for _ in range(m) :
    frm,to = map(int,input().split())
    coms[to].append(frm)
# print(f'{coms=}')

results =[]
max_value = 0
for i,com in enumerate(coms) :
    count = 0
    count = bfs(i,coms,n)
    # print(f'{i=} {count=}')
    if  count > max_value :
        max_value = count
        results = [str(i)]
    elif count == max_value :
        results.append(str(i))

print(' '.join(results))
