
def movecase_r(mtrx,r,c) :
    result  = []
    # 이동
    if  mtrx[r][c+2] == 0  :  # 오른쪽이동
        result.append((r,c+1,'r'))
    if  mtrx[r][c-1] == 0 :  # 왼쪽이동
        result.append((r,c-1,'r'))
    if  mtrx[r+1][c] == 0 and mtrx[r+1][c+1] == 0 :  # 아래쪽이동
        result.append((r+1,c,'r'))    
    if  mtrx[r-1][c] == 0 and mtrx[r-1][c+1] == 0 : # 위쪽이동
        result.append((r-1,c,'r'))    
    
    # 회전
    if  mtrx[r-1][c] == 0 and mtrx[r-1][c+1] == 0 :   # 왼쪽축기준 반시계방향 90도회전
        result.append((r-1,c,'c'))    
    if  mtrx[r-1][c] == 0 and mtrx[r-1][c+1] == 0 :   # 오늘쪽축기준 시계방향 90도회전
        result.append((r-1,c+1,'c'))            
    if  mtrx[r+1][c] == 0 and mtrx[r+1][c+1] == 0 :   # 왼쪽축기준 시계방향 90도회전
        result.append((r,c,'c'))          
    if  mtrx[r+1][c] == 0 and mtrx[r+1][c+1] == 0 :   # 오른쪽축기준  반시계방향 90도회전
        result.append((r,c+1,'c'))    

    return result

def movecase_c(mtrx,r,c) :
    result = []
    # 이동
    if  mtrx[r][c+1] == 0 and mtrx[r+1][c+1] == 0  :  # 오른쪽이동
        result.append((r,c+1,'c'))
    if  mtrx[r][c-1] == 0 and mtrx[r+1][c-1] == 0 :  # 왼쪽이동
        result.append((r,c-1,'c'))
    if  mtrx[r+2][c] == 0 :  # 아래쪽이동
        result.append((r+1,c,'c'))    
    if  mtrx[r-1][c] == 0 : # 위쪽이동
        result.append((r-1,c,'c'))    
        
    # 회전
    if  mtrx[r][c-1] == 0 and mtrx[r+1][c-1] == 0 :   # 위쪽기준 시계방향 90도회전
        result.append((r,c-1,'r'))    
    if  mtrx[r][c+1] == 0 and mtrx[r+1][c+1] == 0 :   # 위쪽기준 반시계방향 90도회전
        result.append((r,c,'r'))            
    if  mtrx[r][c+1] == 0 and mtrx[r+1][c+1] == 0 :   # 아래쪽기준 시계방향 90도회전
        result.append((r+1,c,'r'))          
    if  mtrx[r][c-1] == 0 and mtrx[r+1][c-1] == 0 :   # 아래쪽기준 반시계방향 90도회전
        result.append((r+1,c-1,'r'))   
                      
    return result

def solution(board):
    mtrx = [[1 for _ in range(len(board[0])+2)]  for _ in range(len(board)+2)]
    for i in range(len(board)) :
        for j in range(len(board[0])) :
            mtrx[i+1][j+1] = board[i][j]
    
    # for i in range(len(mtrx)) :
    #     for j in range(len(mtrx[0])) :
    #         print(mtrx[i][j], end=' ')
    #     print('')

    visited = []

    r,c,p = 1,1,'r'
    q = [(r,c,p,0)]
    while (q) :
        # print(q)
        r,c,p,m = q.pop(0)
        if  ( p=='r' and r==len(board) and c+1 == len(board) ) or \
            ( p=='c' and r+1==len(board) and c == len(board) ) :
            return m
        if  (r,c,p) in visited : continue
        visited.append((r,c,p))
        if  p == 'r' :
            result = movecase_r(mtrx,r,c)
        else :
            result = movecase_c(mtrx,r,c)
        for r in result : q.append((*r,m+1))

    answer = 0
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))