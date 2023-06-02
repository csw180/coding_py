# 백준 지름길:1446 https://www.acmicpc.net/problem/1446

import sys

def bfs(start,end) :
    q = [(start,0)]
    tot_cost = []
    while q :
        cur,cost = q.pop(0)
        noway = True
        for i in range(len(shortcuts)) :
            if shortcuts[i][0] >= cur and shortcuts[i][1] <= end:
                noway = False
                q.append((shortcuts[i][1],min(cost + shortcuts[i][0] - cur + shortcuts[i][2],cost + shortcuts[i][1] - cur)))
        if noway :
            tot_cost.append(cost + end - cur)
    return tot_cost

N, D = map(int,sys.stdin.readline().split())

shortcuts = []

for _ in range(N) :
    f,t,e = map(int,sys.stdin.readline().split())
    shortcuts.append((f,t,e))

print(min(bfs(0,D)))