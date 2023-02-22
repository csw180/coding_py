
def solution(cap, n, deliveries, pickups):
    answer = 0

    d = 0
    p = 0

    for i in range(n-1, -1, -1):

        cnt = 0

        d -= deliveries[i]
        p -= pickups[i]

        while d < 0 or p < 0:
            d += cap
            p += cap
            cnt += 1

        answer += (i + 1) * 2 * cnt

    return answer

print(solution(4,5,[1, 0, 30, 0, 0],[0, 4, 0, 8, 0]))
# print(solution(2,7,[1, 0, 2, 0, 1, 0, 2],[0, 2, 0, 1, 0, 2, 0]))

#  실패,시간초과
# from math import ceil

# def rearrange(cap,n,array) :
#     stack = []
#     for i in range(n-1,-1,-1):
#         if not stack or stack[-1][1]%cap == 0 :
#             if array[i] != 0 : stack.append((i+1,array[i]))
#         else :
#             if  array[i]== 0 : continue
#             idx, num =  stack.pop()
#             # print(f'ceil(num/cap)*cap={ceil(num/cap)*cap},num={num}, array[i]={array[i]}')
#             if ceil(num/cap)*cap - num >= array[i] :
#                 stack.append((idx,num + array[i]))
#             else : 
#                 stack.append((idx,ceil(num/cap)*cap))
#                 if array[i] - ceil(num/cap)*cap + num != 0  : stack.append((i+1,(array[i] - ceil(num/cap)*cap + num)))
#     return stack
    
# def solution(cap, n, deliveries, pickups):
#     answer = 0
#     deliveries = rearrange(cap,n,deliveries)
#     pickups = rearrange(cap,n,pickups)
#     # print(f'deliveries={deliveries}')
#     # print(f'pickaup={pickups}')
#     while len(deliveries) > 0 or len(pickups) > 0 :

#         go = deliveries.pop() if len(deliveries) > 0 else (0,0)
#         back = pickups.pop() if len(pickups) > 0 else (0,0)
#         max_value = max(go[0], back[0])
#         if go[1] > cap :
#             deliveries.append(go[0],go[1]-cap)
#         if back[1] > cap :
#             pickups.append(back[0],back[1]-cap)

#         answer += max_value * 2
#     return answer