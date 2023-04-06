def solution(plans):
    answer = []
    plans_x = []
    for  p in sorted(plans,key=lambda x : x[1]):
        tmp_list = p[1].split(':')
        plans_x.append((p[0],int(tmp_list[0]) * 60 + int(tmp_list[1]),int(tmp_list[0]) * 60 + int(tmp_list[1])+int(p[2])))
    # print(f'{plans_x=}')
    remains = []
    current = ('',0)

    for pn, ps, pp in plans_x :
        if  current[1] == 0 :
            current = (pn,pp)
        elif current[1] > ps :
            remains.append((current[0],current[1]-ps))
            current=(pn,pp)
        elif current[1] <= ps :
            answer.append(current[0])  # 직전 과제 answer 에 추가
            while remains and current[1] < ps :   # remain 중 하나 가져와서 처리
                rn,rp = remains.pop();
                if  current[1] + rp > ps :
                    rp = current[1] + rp - ps
                    remains.append((rn,rp))
                    current = (rn,ps)
                else :
                    answer.append(rn)
                    current = (rn,current[1]+rp)
            current = (pn,pp)
        # print(f'{current=},{remains=},{answer=}')

    answer.append(plans_x[-1][0])    
    while remains :
        answer.append(remains.pop()[0])
    return answer

print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))
print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
