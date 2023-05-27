# 백준 시간관리 https://www.acmicpc.net/problem/1263

import sys

n= int(sys.stdin.readline())
jobs = []
for _ in range(n) :
    t, s= map(int,sys.stdin.readline().split(' '))
    jobs.append((s,t))

jobs.sort(reverse=True)
answer = jobs[0][0]
for l, v in jobs :
    answer = min(l,answer) - v

print(answer if answer >= 0 else -1)