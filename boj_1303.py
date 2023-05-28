# 백준 전쟁-전투:1303  https://www.acmicpc.net/problem/1303

# import pprint
import sys

def dfs(start, matrix, visited) :
    pr = [0,0,1,-1]
    pc = [1,-1,0,0]
    r,c  = start
    q = []
    q.append(start)
    ch,cnt = matrix[r][c], 0
    m = len(matrix)
    n = len(matrix[0])
    while q :
        r, c  = q.pop()
        if visited[r][c] :
            continue
        visited[r][c] = True
        cnt += 1
        for k in range(4) :
            if  (0 <= r+pr[k] < m) and (0<= c+pc[k] < n) and \
                (not visited[r+pr[k]][c+pc[k]]) and          \
                matrix[r+pr[k]][c+pc[k]] == ch :
                q.append((r+pr[k],c+pc[k]))    
    return (ch,cnt)

n,m = map(int,sys.stdin.readline().split(' '))
matrix = [['' for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
for i in range(m) :
    inlist = list(sys.stdin.readline().rstrip())
    for j,v in enumerate(inlist) :
        matrix[i][j] = v
        visited[i][j] = False

score_w = 0
score_b = 0
for i in range(m) :
    for j in range(n) :
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