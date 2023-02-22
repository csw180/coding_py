from itertools import permutations

def inspection(lst,case) -> bool :
    s, e = 0,0
    for c in case:
        while e < len(lst):
            if c > (lst[e] - lst[s]) :
                e += 1
            elif c == (lst[e] - lst[s]) :
                e +=1
                s = e
                break
            else :
                s = e
                break
    return True if e >= len(lst) else False

def solution(n, weak, dist):
    answer = []
    len_weak = len(weak)
    weak += [v+n for v in weak]
    
    dist.sort(reverse=True)
    cases = []
    for i in range(1,len(dist)+1) :
        cases.extend(permutations(dist,i))
    
    for  s in range(len_weak) :   # 시작점
        e = s + len_weak
        for case in cases :       # case 별
            if  inspection(weak[s:e],list(case)) :
                answer.append(len(case))

    return min(answer) if answer else -1


# print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))
# print(solution(12,[1, 3, 4, 9, 10],[3, 5, 7]))
# print(solution(16,[1,2,3,4,5,7,8,10,11,12,14,15],[4,2,1,1]))
print(solution(200,[0, 100],[1,1]))


# print(inspection([0, 100],[1,1]))
# print(inspection([5, 6, 10, 13],[4,3,2]))
