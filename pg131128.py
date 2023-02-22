
def solution(X, Y):
    answer =""
    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    return ("0" if answer[0]=='0' else answer)  if answer else "-1"

print(f'case1 = {solution("12321","42531")}')
print(f'case2 = {solution("5525","1255")}')
print(f'case3 = {solution("100","2345")}')
print(f'case4 = {solution("100","203045")}')

# 시간초과 case
# def solution(X, Y):
#     sort_x = sorted(list(X), reverse=True)
#     sort_y = sorted(list(Y), reverse=True)
#     # print(sort_x,sort_y)
#     result = []
#     while( len(sort_x) > 0 and len(sort_y) > 0) :
#         if  sort_x[0] > sort_y[0] :
#             sort_x.pop(0)
#         elif sort_x[0] < sort_y[0] :
#             sort_y.pop(0)
#         else :
#             result.append(sort_x.pop(0))
#             sort_y.pop(0)
#     return str(int(''.join(result))) if result else "-1"
#  #str(int   이렇게 쓰먄 속도 저하

# 시간초과 case
# from collections import Counter

# def solution(X, Y):
#     dx = Counter(X)
#     dy = Counter(Y)
#     result = []
#     for k,v in dx.items() :
#         if dy.get(k) is not None :  result.extend([k]*min(v,dy.get(k)))
#     print(result)    
#     return str(int(''.join(sorted(result,reverse=True)))) if result else "-1"
