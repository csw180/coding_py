from collections import Counter

def solution(topping):
    dict_left = dict()
    dict_remain = Counter(topping)
    approach =[(len(dict_left),len(dict_remain))]

    for v in topping :
        if  v in dict_left :
            dict_left[v] += 1
        else :
            dict_left[v] = 1

        if  dict_remain[v] == 1 :
            del dict_remain[v]
        else :
            dict_remain[v] -= 1
        # print(f'dict_left:{dict_left}  :   dict_remain:{dict_remain}')
        if  len(dict_left) > len(dict_remain) :
            break
        approach.append((len(dict_left),len(dict_remain)))

    # print(f'approach:{approach} ')
    if  approach[-1][0] == approach[-1][1] :
        answer = approach.count(approach[-1])
    else :
        answer = 0
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))
print(solution([1]))

