from collections import Counter

def solution(want, number, discount):
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
    
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == check:
            answer += 1

    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"],[3, 2, 2, 2, 1],["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"],[10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))

#  11번 케이스만 오류 발생
# def solution(want, number, discount):
#     answer = 0
#     want_dic = dict()
#     for i in range(len(want)) :
#         want_dic[want[i]]=number[i]

#     discount_dict = dict()
#     for i in range(10):
#         if discount_dict.get(discount[i]) is None :
#             discount_dict[discount[i]] = 1
#         else :
#             discount_dict[discount[i]] +=1
#     start = 0
#     last = start+9

#     while (last+1<len(discount)) :
#         start +=1
#         last +=1
#         discount_dict[discount[start-1]] -= 1
#         if discount_dict.get(discount[last]) is None :
#             discount_dict[discount[last]] = 1
#         else :
#             discount_dict[discount[last]] +=1

#         enough = True
#         for k,v in want_dic.items()     :
#             if (discount_dict.get(k) is None) or (discount_dict[k] < v) :
#                 enough = False
#                 break
#         if enough : answer +=1
    
#     return answer