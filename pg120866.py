
# 프로그래머서 코딩테스트 연습 > 코딩테스트 입문 > 안전지대 (120866)
# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def danger_idx(bomb_idx, w) :
    """
    폭탄위치(bomb_idx)를 중심으로 왼위, 위, 오른위, 왼, 폭탄, 오른, 왼아래, 아래, 오른아래를 
    위험위치(danger_pos)에 담아서 return 한다
    """
    r,c = bomb_idx
    danger_pos = []
    if r > 0 and c > 0 :
        danger_pos.append((r-1,c-1))
    if r > 0 :
        danger_pos.append((r-1,c))
    if r > 0 and c < w-1 :
        danger_pos.append((r-1,c+1))

    if c > 0:
        danger_pos.append((r,c-1))
    danger_pos.append((r,c))
    if c < w-1 :
        danger_pos.append((r,c+1))
     
    if r < w-1 and c > 0 :
        danger_pos.append((r+1,c-1))
    if r < w-1 :
        danger_pos.append((r+1,c))
    if r < w-1 and c < w-1 :
        danger_pos.append((r+1,c+1))
    # print(f'danger_idx : danger_pos = {danger_pos}')
    return danger_pos

def solution(board):
    w = len(board)
    danger_pos = []
    bomb_idxs = [ (i,j) for i in range(w) for j in range(w) if board[i][j]==1]
    for v in bomb_idxs :
        rtn = danger_idx(v,w)
        danger_pos.extend(rtn)

    # print(danger_pos)
    return w*w - len(set(danger_pos))


print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))