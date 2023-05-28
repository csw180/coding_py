# 백준 전쟁-전투:1303  https://www.acmicpc.net/problem/1303
# 일부 case 에 대하여 IndexError 발생  원인못찾음 ㅠ

import pprint
import sys

def dfs(start, matrix, visited) :
    pr = [0,0,1,-1]
    pc = [1,-1,0,0]
    r,c  = start
    q = []
    q.append(start)
    ch,cnt = matrix[r][c], 0
    while q :
        r, c  = q.pop()
        if visited[r][c] :
            continue
        visited[r][c] = True
        cnt += 1
        for k in range(4) :
            if (not visited[r+pr[k]][c+pc[k]]) and matrix[r+pr[k]][c+pc[k]] == ch :
                q.append((r+pr[k],c+pc[k]))    
    return (ch,cnt)

n,m = map(int,sys.stdin.readline().split(' '))
matrix = [['' for _ in range(m+2)] for _ in range(n+2)]
visited = [[True for _ in range(m+2)] for _ in range(n+2)]
for i in range(1,n+1) :
    inlist = list(sys.stdin.readline().rstrip())
    for j,v in enumerate(inlist,1) :
        matrix[i][j] = v
        visited[i][j] = False
# print('---------------------')
# pprint.pprint(matrix)
# pprint.pprint(visited)                
# print('---------------------')

score_w = 0
score_b = 0
for i in range(1,n+1) :
    for j in range(1,m+1) :
        if  not visited[i][j] :
            ch, cnt = dfs((i,j), matrix, visited)
            # print('---------------------')
            # pprint.pprint(matrix)
            # pprint.pprint(visited)                
            # print('---------------------')
            if ch == 'W' :
                score_w += cnt**2
            else  :
                score_b += cnt**2
            
print(f'{score_w} {score_b}')