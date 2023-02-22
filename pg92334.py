def solution(id_list, report, k):
    answer = []
    accused_dic = { i : [] for i in id_list }
    accuse_dic = { i : 0 for i in id_list }
    for r  in report :
        splited_r = r.split(' ') 
        if splited_r[0] not in accused_dic[splited_r[1]] :
            accused_dic[splited_r[1]].append(splited_r[0])
    # print(f'{accused_dic=}')

    for key,val in accused_dic.items() :
        if len(val) >= k :
            for v in val : 
                accuse_dic[v] +=1
    # print(f'{accuse_dic=}')

    for i in id_list :
        answer.append(accuse_dic[i])
    return answer


# print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],	["ryan con", "ryan con", "ryan con", "ryan con"],3))
