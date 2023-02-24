def solution(board):
    board_ = []
    board_.append(list(board[0]))
    board_.append(list(board[1]))
    board_.append(list(board[2]))

    o_cnt, o_win, x_cnt, x_win = 0, False, 0, False

    if board[0][0] == board[1][1] == board[2][2] :
        if board[0][0] == 'O' :      o_win = True
        elif board[0][0] == 'X' :    x_win = True
    if board[0][2] == board[1][1] == board[2][0] :
        if board[0][2] == 'O' :      o_win = True
        elif board[0][2] == 'X' :    x_win = True        
    for i in range(3) :
        if  board[i][0] == board[i][1] == board[i][2] :
            if board[i][0] == 'O' :      o_win = True
            elif board[i][0] == 'X' :    x_win = True
        if  board[0][i] == board[1][i] == board[2][i] :
            if board[0][i] == 'O' :      o_win = True
            elif board[0][i] == 'X' :    x_win = True

        for j in range(3) :
            if  board[i][j] == 'O' :
                o_cnt +=1
            elif board[i][j] == 'X' :
                x_cnt +=1
    # print(f'{o_cnt=}, {o_win=}, {x_cnt=}, {x_win=}')

    answer = 1
    if o_win and (not x_win) :
        if o_cnt != x_cnt + 1 :
            answer = 0
    if o_win and x_win :
        answer = 0
    if (not o_win)  and x_win :
        if o_cnt != x_cnt :
            answer = 0
    if (not o_win) and (not x_win) :
        if not ((o_cnt == x_cnt) or (o_cnt == x_cnt + 1)) :
            answer = 0

    return answer

print(solution(["O.X", ".O.", "..X"]))
# print(solution(["OOO", "...", "XXX"]))
# print(solution(["...", ".X.", "..."]))
# print(solution(["...", "...", "..."]))