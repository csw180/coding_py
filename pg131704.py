def solution(order):
    sub = []
    if order[0] > 1 :  sub.append([1,order[0]-1])
    # print(f'order[idx]={order[0]},sub={sub}')
    max_value = order[0]
    for idx in range(1,len(order)) :
        if  order[idx] > max_value :
            if max_value+1 < order[idx] :
                sub.append([max_value+1,order[idx]-1])
            max_value = order[idx]
        elif  order[idx] == sub[-1][1] :
            temp = sub.pop()
            if temp[0]<temp[1] :
                sub.append([temp[0],temp[1]-1])
        else :
            return idx
        # print(f'order[idx]={order[idx]},sub={sub}')
    return len(order)

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
print(solution([16, 15, 17, 14, 10]))
print(solution([1, 2, 4, 3, 5] ))

# 시간초과 case
# def solution(order):
#     for idx in range(1,len(order)) :
#         if  order[idx] > order[idx-1] or order[idx]+1 in order[:idx] :
#             continue
#         else :
#             return idx
#     return len(order)