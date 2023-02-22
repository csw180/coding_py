def solution(n, lost, reserve):
    answer = []
    d = []
    lost_n = 0
    for v in lost : 
        if v not in reserve :
            lost_n += 1
            d.append((v,0))

    for v in reserve :
        if v not in lost : d.append((v,1))

    sorted_d = sorted(d,key=lambda x: (x[0],x[1]))
    prev_n, prev_type = 0,-1
    while sorted_d :
        cn, type = sorted_d.pop(0)
        # print(f'prev_n={prev_n},prev_type={prev_type},cn={nc},type={type}')
        if  (prev_n == 0) or (prev_n+1) < cn or (prev_type == type):
            prev_n, prev_type = cn, type
        elif (prev_n+1 == cn)  and (prev_type != type) :
            answer.append((prev_n,cn))
            prev_n, prev_type = 0,-1
    return n - lost_n + len(answer)


print(solution(5,[2, 4],[1, 3, 5]))
print(solution(8,[2, 4, 5],[1, 3, 5]))
# print(solution(5,[2, 4],[3]))
# print(solution(3,[3],[1]))