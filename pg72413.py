def dijkstra(n,fares,s) :
    distince = [float('inf') for i in range(n+1)]
    visited =[]

    adj_dic = {}
    for v in fares :
        if adj_dic.get(v[0]) is None :
            adj_dic[v[0]] = [(v[2],v[1])]
        else :
            adj_dic[v[0]].append((v[2],v[1]))

    distince[s] = 0
    current = s

    while current :
        visited.append(current)
        adj_list = adj_dic[current]
        # print(f'{current=}, {adj_list=}, {visited=}')
        for i in adj_list :
            if distince[i[1]] > (distince[current] + i[0]) and i[1] not in visited:
                distince[i[1]] = distince[current] + i[0]

        min_value, min_idx = float('inf'),0
        for  i,d in enumerate(distince) :
            if (d < min_value) and (i not in visited) :
                min_value, min_idx = d, i
            # print(f'{i=},{d=}, {min_value=} {min_idx=}')
        current = min_idx
        # print(f'{distince=}, {current=}')
    return distince

def solution(n, s, a, b, fares):
    fares += list(map(lambda x : [x[1],x[0],x[2]]  , fares))
    jointway = dijkstra(n,fares,s)
    # print(f'{jointway=}')
    a_way  = dijkstra(n,fares,a)
    # print(f'{a_way=}')
    b_way  = dijkstra(n,fares,b)
    # print(f'{b_way=}')
    answer = 0

    min_value  = float('inf')
    for k in range(1,n+1):
        if min_value >  jointway[k] + a_way[k] + b_way[k] :
            min_value = jointway[k] + a_way[k] + b_way[k]
    
    return min_value


# fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
# print(solution(6,4,6,2,fares))
fares = 	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(7,3,4,1,fares))
# fares = 	[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
# print(solution(6,4,5,6,fares))
