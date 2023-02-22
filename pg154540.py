def bfs(lst_map,me) :
    w,h = len(lst_map[0]),len(lst_map)
    r,c = me
    queue = []
    queue_sum = 0

    queue.append(me)
    queue_sum += int(lst_map[r][c])
    lst_map[r][c] ='X'

    while queue :
        r,c = queue.pop(0)
        # print(r,c,queue)
        if r>0 and lst_map[r-1][c] != "X" :
            queue.append((r-1,c))
            queue_sum += int(lst_map[r-1][c])
            lst_map[r-1][c] ='X'
        if r<h-1 and lst_map[r+1][c] != "X" :
            queue.append((r+1,c))
            queue_sum += int(lst_map[r+1][c])
            lst_map[r+1][c] ='X'
        if c>0 and lst_map[r][c-1] != "X" :
            queue.append((r,c-1))
            queue_sum += int(lst_map[r][c-1])
            lst_map[r][c-1] ='X'            
        if c<w-1 and lst_map[r][c+1] != "X" :
            queue.append((r,c+1))
            queue_sum += int(lst_map[r][c+1])
            lst_map[r][c+1] ='X'               
    return  queue_sum

def solution(maps):
    lst_map = [list(v) for v in maps ]
    w,h = len(lst_map[0]),len(lst_map)
    # print(f"lst_map= {lst_map}")
    sum_list = []
    for r in range(h) :
        for c  in range(w):
            if  lst_map[r][c] != "X" :
                sum_list.append(bfs(lst_map,(r,c)))
    if len(sum_list) > 0 : 
        sum_list.sort()
    else :
        sum_list.append(-1)  
    return sum_list


print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))


