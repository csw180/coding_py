import sys

R,C,K =  map(int,sys.stdin.readline().rstrip().split(' '))

board = []
board.append('#'*(C+2))
for i in range(R):
    board.append('#' + sys.stdin.readline().rstrip() + '#')
board.append('#'*(C+2))

start, end = (R,1), (1,C)
ways = []
ways.append(start)
q = []
q.append(ways)
result = []
while q :
    way = q.pop()
    if way[-1] == end :
        result.append(len(way))  
        continue
    r,c = way[-1]
    if board[r-1][c] == '.' and (r-1,c) not in way :
        q.append(way + [(r-1,c)])
    if board[r+1][c] == '.' and (r+1,c) not in way :
        q.append(way + [(r+1,c)])
    if board[r][c-1] == '.' and (r,c-1) not in way :
        q.append(way + [(r,c-1)])
    if board[r][c+1] == '.' and (r,c+1) not in way :
        q.append(way + [(r,c+1)])
    # print(q)
print(result.count(K))