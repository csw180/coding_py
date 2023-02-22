def solution(common):
    one, two, three = common[:3]
    if two - one == three - two:
        result = common[-1] + (two-one)
    elif two // one == three // two:
        result = common[-1] * (two//one)  
    return result

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
print(solution([-3, 6, -12, 24,-48]))

# 1개 case 오류
# def solution(common):
#     ap = common[2] - common[1]  # 등차
#     gp = common[2] / common[1]  # 등비

#     ap_ary = [ common[0] + (ap*i) for i in range(len(common)+1)]
#     gp_ary = [ int(common[0] * (gp**i)) for i in range(len(common)+1)]
#     print(f'ap_ary={ap_ary},gp_ary={gp_ary}')

#     if  common == ap_ary[:len(common)] :
#         return ap_ary[len(common)]
#     else :
#         return gp_ary[len(common)]