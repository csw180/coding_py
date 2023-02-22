from itertools import combinations

def get_score(anermy: list, me:list) -> int :
    anermy_score = 0 
    me_score = 0
    for i in range(len(anermy)) :
        if anermy[i] >= me[i] :
            if anermy[i] == 0 and me[i] == 0 :
                continue
            else :
                anermy_score += 10-i
        else :
            me_score += 10-i
    return (-1) * (anermy_score - me_score) if anermy_score >= me_score else (me_score - anermy_score)

def solution(n, info):
    ps = []       # 승패패패패..., 승승패패패.., 승승승패패패 .. case 롤 모두나눈다.
    for i in range(1,n+1) :
        ps.extend(combinations([k for k in range(len(info)-1)],i))

    max_value = 0
    max_list = []
    for p in ps :

        # 각 case를 info 와 같은 형식의 list 로 만든다.
        pcount = [0 for i in range(len(info))]
        for v in  p : pcount[v] = info[v] + 1
        if  n - sum(pcount) >= 0 :
            pcount[10] = n - sum(pcount)
        else :    # 해당 case 가 쏠 수 있는 화살수(n)를 초과하는 경우는 고려할 case가 아니므로 pass
            continue
        
        tmp_value  = get_score(info, pcount) # 점수구한다.
        if tmp_value > max_value and tmp_value > 0:  #점수차가 최대로 나는 case만 max_list 에 삽입
            max_value = tmp_value 
            max_list = []
            max_list.append(pcount)
        elif tmp_value == max_value and tmp_value > 0:
            if pcount not in max_list : max_list.append(pcount)

    if  max_list :
        max_list.sort(key=lambda x : ''.join(map(str,x[::-1])),reverse=True)
        return max_list[0]
    else : 
        return [-1]

# return list(sorted(list(map(lambda t: ''.join(list(map(str,t)))[::-1],max_list)),reverse=True)[0]) if max_list else [-1]
# print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1,[1,0,0,0,0,0,0,0,0,0,0]))
# print(solution(9,	[0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10,	[0,0,0,0,0,0,0,0,3,4,3]))
