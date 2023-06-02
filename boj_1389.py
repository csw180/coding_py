# 백준 케빈케이번의 6단계법칙:1389 https://www.acmicpc.net/problem/1389

import sys

def bfs(start):
    queue = [(start,0)]
    visited = [False] * (N+1)
    distance = 0
    while queue:
        # print(f'{start=} {queue=}')
        now, cnt = queue.pop(0)
        if visited[now]:
            continue
        visited[now] = True
        distance += cnt
        for i in relations[now]:
            if not visited[i]:
                queue.append((i,cnt+1))
    return distance

N, M = map(int,sys.stdin.readline().split())

relations = dict()
for _ in range(M):
    a, b = map(int,sys.stdin.readline().split())
    if relations.get(a) :
        relations[a].append(b)
    else :
        relations[a] = [b]

    if relations.get(b) :
        relations[b].append(a)
    else :
        relations[b] = [a]

min_value = float('inf')
min_index = 0
for k in sorted(relations.keys()):
    distance = bfs(k)
    if distance < min_value:
        min_value = distance
        min_index = k

print(min_index)