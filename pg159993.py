def bfs(visited,start,lever, ex) :
    q = []
    q.append((*lever,0))

    ns = []
    while q:
        r, c, n = q.pop(0)
        if visited[r][c] =='X' :
            continue
        if ((r,c) == start) or ((r,c) == ex):
            ns.append(n)
        visited[r][c] = 'X'
        if visited[r][c+1] == 'O' :
            q.append((r,c+1,n+1))
        if visited[r-1][c] == 'O' :
            q.append((r-1,c,n+1))
        if visited[r][c-1] == 'O' :
            q.append((r,c-1,n+1))
        if visited[r+1][c] == 'O' :
            q.append((r+1,c,n+1))            
    return sum(ns) if len(ns) == 2 else -1

def solution(maps):
    board = [['X' for _ in range(len(maps[0])+2)] for _ in range(len(maps)+2)]
    start, lever, ex  = None, None, None
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            board[i+1][j+1] = maps[i][j]

            if  board[i+1][j+1] == 'S' :
                start = (i+1,j+1)
                board[i+1][j+1] = 'O'
            elif board[i+1][j+1] == 'L' :
                lever = (i+1,j+1)
                board[i+1][j+1] = 'O'
            elif board[i+1][j+1] == 'E' :
                ex = (i+1,j+1)
                board[i+1][j+1] = 'O'

    return bfs(board,start,lever,ex)

# print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))
print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]))

# def solution(maps):
#     board = [['X' for _ in range(len(maps[0])+2)] for _ in range(len(maps)+2)]
#     map_board = []
#     for map in maps :
#         map_board.append(list(map))

#     start, lever, ex  = None, None, None
#     for i in range(len(map_board)) :
#         for j in range(len(map_board[0])) :
#             board[i+1][j+1] = map_board[i][j]
#             if  board[i+1][j+1] == 'S' :
#                 start = (i+1,j+1)
#                 board[i+1][j+1] = 'O'
#             elif board[i+1][j+1] == 'L' :
#                 lever = (i+1,j+1)
#                 board[i+1][j+1] = 'O'
#             elif board[i+1][j+1] == 'E' :
#                 ex = (i+1,j+1)
#                 board[i+1][j+1] = 'O'

#     visited = copy.deepcopy(board)
#     n1 = bfs(visited,start,lever)
#     if n1==-1 :  return -1

#     visited = copy.deepcopy(board)
#     n2 = bfs(visited,lever,ex)
#     if n2==-1 :  return -1

#     return n1 + n2