def movable(r,c,board) :
    result =[]

    #왼쪽
    rr = r
    cc = c
    while cc>0 and board[rr][cc-1] != 'D' :  cc-=1
    if c!=cc : result.append((rr,cc))

    #오른쪽
    rr = r
    cc = c
    while cc<len(board[0])-1 and board[rr][cc+1] != 'D' :  cc+=1
    if c!=cc : result.append((rr,cc))

    #위쪽
    rr = r
    cc = c
    while rr>0 and board[rr-1][cc] != 'D' :  rr-=1
    if r!=rr : result.append((rr,cc))

    #아래쪽
    rr = r
    cc = c
    while rr<len(board)-1 and board[rr+1][cc] != 'D' :  rr+=1
    if r!=rr : result.append((rr,cc))

    return result

def bfs(r,c,board) :
    q = []
    visit = [[0 for i in range(len(board[0]))] for j in range(len(board))]
    q.append((r,c,0))
    while q :
        pr, pc, cnt  = q.pop(0)
        if board[pr][pc] == 'G' : return cnt
        if visit[pr][pc] == 1 : continue
        visit[pr][pc] = 1
        result = movable(pr, pc,board)
        for tr, tc in result :
            q.append((tr,tc,cnt+1))
    return -1

def solution(board):
    rr, rc = 0 ,0
    for i in range(len(board)) :
        if board[i].find('R') != -1 :
            rr = i
            rc = board[i].find('R')
            break

    return bfs(rr,rc,board)

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	))
# print(solution([".D.R", "....", ".G..", "...D"]	))

