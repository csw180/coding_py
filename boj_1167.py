import sys

n = int(sys.stdin.readline())
graph = {i:list() for i in range(1,n+1)}
for _ in  range(n) :
    lin = list(map(int,sys.stdin.readline().split(' ')))
    for i in range((len(lin)-2)//2) :
        graph[lin[0]].append((lin[2*i+1],lin[2*i+2]))

print(graph)
