# from collections import Counter
# def solution(lines):
#     answer =0
#     tlist =[]
#     for v in lines :
#         tlist.extend(range(v[0],v[1]))
#     c = Counter(tlist)
#     for k,v in c.items() :
#         if v>=2 :
#             answer+=1
#     return answer

def solution(lines):
    answer =0
    tdict = dict()
    for v in lines :
        for i in range(v[0],v[1]) :
            if tdict.get(i) is None :
                tdict[i] = 0
            tdict[i] += 1
    return len(list(filter(lambda x : x[1] >=2, tdict.items())))

print(solution([[0, 5], [3, 9], [1, 10]]))
print(solution([[-1, 1], [1, 3], [3, 9]]))
print(solution([[0, 1], [2, 5], [3, 9]]))
