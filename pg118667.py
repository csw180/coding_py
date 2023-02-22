'''
합이 큰쪽 큐에서 원소를 빼서 합이 작은쪽 큐로 옮기는 과정을 반복하면서 
값이 일치하는 시점을 찾는 방식
'''
def solution(queue1, queue2):    
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    pos_q1 = 0
    pos_q2 = 0

    move_cnt = 0
    queue1, queue2 = queue1 + queue2 , queue2 + queue1
    while True :
        if sum_q1 > sum_q2 :
            if pos_q1 >= len(queue1) :
                return -1
            # print(f'{sum_q1}:{sum_q2} q1->q2 value:{queue1[pos_q1]}')
            sum_q1 -= queue1[pos_q1]
            sum_q2 += queue1[pos_q1]
            pos_q1 += 1
            move_cnt +=1
        elif sum_q1 < sum_q2 :
            if pos_q2 >= len(queue2) :
                return -1
            # print(f'{sum_q1}:{sum_q2} q2->q1 value:{queue2[pos_q2]}')
            sum_q2 -= queue2[pos_q2]
            sum_q1 += queue2[pos_q2]
            pos_q2 += 1
            move_cnt +=1
        else :
            break
    # print(f'{sum_q1=} {sum_q2=}')        
    return move_cnt


# print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
# print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
print(solution([1,1],[1,5]))
