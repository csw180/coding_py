import sys
from  heapq import *

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = {i:list() for i in range(1,n+1)}
for i in range(m) :
    s,e,c = map(int,sys.stdin.readline().split(' '))
    graph[s].append((e,c))

print(f'graph info = {graph}')        
start, end = map(int,sys.stdin.readline().split(' '))
print(f'{start=}, {end=}')        

INF = int(1e9)
distance = [INF for _ in range(n+1)]
distance[start] = 0

q = []
heappush(q,(0,start))

while q :
    fee, current  = heappop(q)
    print(f'({fee},{current}),{q=},{distance=}')

    if  fee > distance[current] :
        continue

    for e, c  in graph[current] :
        if  distance[e] > distance[current] + c :
            distance[e]  = distance[current] + c
            heappush(q,(distance[e],e))
        
print(distance[end])
